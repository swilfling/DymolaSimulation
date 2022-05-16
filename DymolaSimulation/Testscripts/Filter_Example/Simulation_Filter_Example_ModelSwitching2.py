import os
from DymolaSimulation.SimulationUtilities.Parameters import SimulationParameters, InitializationParameters
from DymolaSimulation.Simulation.DymolaSimulator import DymolaSimulator

if __name__ == "__main__":
    package_path = os.path.abspath("../../DymolaTemplates/DymolaExamples")

    # Simulation Parameters
    simulation_parameters = SimulationParameters(algorithm="Dassl",
                                                 start_time=0,
                                                 # stop_time=2.8854e+07,
                                                 stop_time=100,
                                                 output_interval=0.01)

    # Parameter Definitions
    package_name = "DymolaExamples.Examples_Filters"
    model_name = "Test_Model_Filters_ModelSwitching_2"
    output_file_name = "result_filters"

    # ################ Simulation ############################################################

    plot_enabled = True
    store_results_to_csv = True
    use_init_condition = True

    # Optional: Dymola Path
    dymolapath = os.environ.get("DYMOLAPATH")

    simulator = DymolaSimulator(workdir_path=package_path,
                                package_paths_full=[os.path.join(package_path,"package.mo")],
                                package_name=package_name,
                                model_name=model_name,
                                result_root_dir=package_path,
                                sim_params=simulation_parameters,
                                initialization_parameters=InitializationParameters(),
                                result_filename=output_file_name,
                                dymolapath=dymolapath)

    # Variables to plot
    plotting_variables = ["InputSignal.y", "filter_output.y"]

    fmu_dir = os.path.join(package_path, "FMUOutput")
    fmu_paths = [os.path.join(fmu_dir, "Butterworth.fmu"), os.path.join(fmu_dir, "Chebyshev.fmu")]
    # Setup
    simulator.setup_experiment(exp_name="ModelSwitching", fmu_paths_full=fmu_paths)
    # First exp: butterworth
    simulator.run_experiment(exp_name="Butterworth", trajectory_names=plotting_variables, start_time=0, stop_time=50)

    # Switch to Chebyshev
    commands = ["selector.k=2"]
    simulator.execute_commands(commands, "model_switching_script.mos")

    # Run Experiment
    simulator.use_init_file()
    simulator.set_init_file("result_filters_Butterworth")
    simulator.run_experiment(start_time=50, stop_time=100, exp_name="Chebyshev", trajectory_names=plotting_variables)

    # Switch back
    commands = ["selector.k=1"]
    simulator.execute_commands(commands, "model_switching_script.mos")

    # Run Experiment
    simulator.set_init_file("result_filters_Chebyshev")
    simulator.run_experiment(start_time=100, stop_time=150, exp_name="Butterworth_2", trajectory_names=plotting_variables)

    simulator.terminate()
