import os
from DymolaSimulation.Simulation.SimulationUtilities.Parameters import SimulationParameters, InitializationParameters, DymolaModelParameters
from DymolaSimulation.Simulation.Simulator import DymolaSimulator

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

    # Create commands and simulate
    simulator.setup_experiment(exp_name="1", fmu_paths_full=[os.path.abspath("../../DymolaTemplates/DymolaExamples/FMUOutput/Chebyshev.fmu")])
    # Adapt parameters
    simulator.run_experiment(exp_name="1", trajectory_names=plotting_variables, start_time=0, stop_time=2,
                             plot_enabled=True)


    simulator.terminate()
