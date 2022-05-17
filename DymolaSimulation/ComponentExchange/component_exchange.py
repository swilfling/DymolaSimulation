import DymolaSimulation.ComponentExchange.exchg_utils as exchg_utils
from DymolaSimulation.SimulationUtilities.Parameters import SimulationParameters, DymolaModelParameters
from DymolaSimulation.Simulation import ModelicaSimulator
from typing import List
import os


class ComponentExchange:
    """
    Implementation of component exchange.
    Parameters:
        - Simulator
        - Dymola model parameters - list of params
        - Time delta between exchange runs - default 1

    Functions:
        Main:
        - run_exchange
        Helper functions:
        - get_initial_exchg_models
        - exchange_models
        - get_exchange_models
        - get_fmu_paths
        - get_package_paths
    """
    time_delta = 1
    models: List[DymolaModelParameters]
    simulator: ModelicaSimulator = None

    def __init__(self, simulator, models: List[DymolaModelParameters], time_delta=1):
        self.simulator = simulator
        self.models = models
        self.time_delta = time_delta

    ######################################### Main function ############################################################

    def run_exchange(self, list_sim_params: List[SimulationParameters], plot_vars, init_mapping):
        '''
        Main function for running component exchange.
        @param list_sim_params: list of simulation parameters for scheduling algorithm.
            For threshold method: pass list with only one element.
        @param plot_vars: variables to plot
        @param init_mapping: Mapping from outputs to inputs for setting of initial values
        @return list of simulation results
        '''
        self.simulator.setup_experiment(exp_name="ModelSwitching", package_paths=self._get_package_paths(),
                                        fmu_paths_full=self._get_fmu_paths())
        exp_cnt = 0
        list_results = []
        start_variables = {}
        current_model, new_model = self._get_initial_exchg_models()
        for sim_params in list_sim_params:
            if current_model.use_fmi_init_params:
                self.simulator.use_init_vals()
                start_variables.update(exchg_utils.create_FMI_init_variables(sim_params))
                self.simulator.set_init_variables(start_variables)
            self.simulator.set_sim_params(sim_params)
            expected_stop_time = sim_params.stop_time
            terminate_time = sim_params.start_time
            while exchg_utils.early_termination(terminate_time, self.time_delta, self.simulator.get_output_interval(), expected_stop_time):
                # Run simulation
                simulation_results = self.simulator.run_experiment(str(exp_cnt), plot_vars, plot_enabled=False)
                # Get termination time
                terminate_time = max(self.simulator.get_start_time(), exchg_utils.get_final_time(simulation_results))
                if terminate_time < expected_stop_time:
                    print(f"Early Termination: Time at termination: {terminate_time}")
                # Switch components
                exchg_utils.switch_components(self.simulator, current_model, new_model)
                current_model, new_model = self._switch_models(current_model, new_model)
                # Init parameters
                start_variables.update(exchg_utils.get_start_vals(simulation_results, init_mapping))
                self.simulator.set_start_time(terminate_time + self.time_delta)
                if current_model.use_fmi_init_params:
                    start_variables.update(exchg_utils.create_FMI_init_variables(self.simulator.sim_params))
                self.simulator.set_init_params_full(f"{self.simulator.result_filename}_{exp_cnt}", start_variables)
                # Store simulation results
                list_results.append(simulation_results)
                exp_cnt += 1

        return list_results

    ######################################## Internal helper methods ###################################################

    def _get_initial_exchg_models(self):
        initial_model = [model for model in self._get_exchange_models() if model.is_initial_exchange_model][0]
        exchange_model = [model for model in self._get_exchange_models() if model != initial_model][0]
        return initial_model, exchange_model

    def _get_exchange_models(self):
        exchg_models = [model for model in self.models if model.is_exchange_model]
        if len(exchg_models) < 2:
            raise Exception("There should be at least 2 models for component exchange.")
        return exchg_models

    def _switch_models(self, current_model, new_model):
        return new_model, current_model

    def _get_fmu_paths(self):
        return [model.fmu_path for model in self.models if model.is_fmu]

    def _get_package_paths(self):
        paths = []
        for model in self.models:
            if model.package_paths is not None:
                for path in model.package_paths:
                    paths.append(path)
        paths = list(set(paths))
        return [os.path.abspath(path) for path in paths]
