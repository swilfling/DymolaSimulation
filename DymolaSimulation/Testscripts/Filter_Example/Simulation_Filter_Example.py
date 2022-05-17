import os
from DymolaSimulation.SimulationUtilities.Parameters import SimulationParameters
from DymolaSimulation.Simulation import DymolaSimulator

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
    model_name = "Test_Model_Filters"
    output_file_name = "result_filters"

    # ################ Simulation ############################################################

    # Optional: Dymola Path
    dymolapath = os.environ.get("DYMOLAPATH")
    result_root_dir = os.path.join(package_path, "Filter_Example")
    os.makedirs(result_root_dir, exist_ok=True)

    simulator = DymolaSimulator(workdir_path=package_path,
                                package_paths_full=[os.path.join(package_path,"package.mo")],
                                package_name=package_name,
                                model_name=model_name,
                                result_root_dir=result_root_dir,
                                sim_params=simulation_parameters,
                                result_filename=output_file_name,
                                dymolapath=dymolapath)

    # Variables to plot
    plotting_variables = ["model_Filters.y", "InputSignal.y"]

    # Create commands and simulate
    simulator.setup_experiment(exp_name="1")
    # Adapt parameters
    simulator.run_experiment(exp_name="1", trajectory_names=plotting_variables, start_time=0, stop_time=2)
    simulator.use_init_file()
    simulator.set_init_file("result_filters_1")
    simulator.run_experiment(start_time=2, stop_time=4, exp_name="2", trajectory_names=plotting_variables)
    simulator.set_init_file("result_filters_2")
    simulator.run_experiment(start_time=4, stop_time=6, exp_name="3", trajectory_names=plotting_variables)
    # Comparison: Full experiment
    simulator.use_init_file(False)
    simulator.run_experiment(start_time=0, stop_time=6, exp_name="Full", trajectory_names=plotting_variables)
    simulator.terminate()
