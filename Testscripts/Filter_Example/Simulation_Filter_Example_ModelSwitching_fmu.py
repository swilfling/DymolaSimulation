import os
from DymolaSimulation.SimulationUtilities.Parameters import SimulationParameters, InitializationParameters, DymolaModelParameters
from DymolaSimulation.Simulation.DymolaSimulator import DymolaSimulator
from DymolaSimulation.ComponentExchange.component_exchange import ComponentExchange

if __name__ == "__main__":
    package_path = os.path.abspath("../../DymolaTemplates/DymolaExamples")

    # Simulation Parameters
    simulation_parameters = SimulationParameters(algorithm="Dassl",
                                                 start_time=0,
                                                 # stop_time=2.8854e+07,
                                                 stop_time=100,
                                                 num_intervals=200)

    # Parameter Definitions
    package_name = "DymolaExamples.Examples_Filters"
    model_name = "Test_Model_Filters_ModelSwitching_fmu"
    output_file_name = "result_filters"

    # ################ Simulation ############################################################

    # Optional: Dymola Path
    dymolapath = os.environ.get("DYMOLAPATH")

    # Settings: Extract end values to set start values
    init_variables = {"y_start":0}

    initialization_parameters = InitializationParameters(use_init_values=True, init_variables=init_variables)
    result_root_dir = os.path.join(package_path, "Filter_Example_ModelSwitching_fmu")
    os.makedirs(result_root_dir, exist_ok=True)

    simulator = DymolaSimulator(workdir_path=result_root_dir,
                                package_paths_full=[os.path.join(package_path,"package.mo")],
                                package_name=package_name,
                                model_name=model_name,
                                result_root_dir=result_root_dir,
                                sim_params=simulation_parameters,
                                initialization_parameters=initialization_parameters,
                                result_filename=output_file_name,
                                dymolapath=dymolapath)

    # Variables to plot
    fmu_instance_name = "UUT"
    plotting_variables = [f"{fmu_instance_name}.u1", f"{fmu_instance_name}.y1"]

    init_mapping = {"y_start": "UUT.y1"}

    params_filt1 = DymolaModelParameters(fmu_path=os.path.join(package_path, "FMUOutput", f"Chebyshev.fmu"),
                                         model_name=f"Chebyshev_fmu",
                                         parameters={"y_start":"y_start",
                                                     "fmi_StartTime":"fmi_StartTime",
                                                     "fmi_StopTime":"fmi_StopTime",
                                                     "fmi_NumberOfSteps":"fmi_NumberOfSteps",
                                                     "fmi_forceShutDownAtStopTime":"true"},
                                         is_fmu=True,
                                         is_exchange_model=True,
                                         use_fmi_init_params=True,
                                         is_initial_exchange_model=True)

    params_filt2 = DymolaModelParameters(fmu_path=os.path.join(package_path, "FMUOutput", f"Butterworth.fmu"),
                                         model_name=f"Butterworth_fmu",
                                         is_fmu=True,
                                         use_fmi_init_params=True,
                                         parameters={"y_start":"y_start",
                                                     "fmi_StartTime": "fmi_StartTime",
                                                     "fmi_StopTime": "fmi_StopTime",
                                                     "fmi_NumberOfSteps": "fmi_NumberOfSteps",
                                                     "fmi_forceShutDownAtStopTime": "true"
                                                     },
                                         is_exchange_model=True)
    dymola_models = [params_filt1, params_filt2]

    simulation_parameters_list = SimulationParameters.create_simulation_parameters(num_experiments=2,start_time=0,start_duration=10, experiment_duration=10,timestep=0.05)
    exchg = ComponentExchange(simulator, dymola_models)
    list_simulation_results = exchg.run_exchange(simulation_parameters_list, plotting_variables, init_mapping)
    simulator.plot_multiple_results(list_simulation_results, set_colormap=True, colors='Set1')
    simulator.terminate()
