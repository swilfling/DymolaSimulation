import os
from DymolaSimulation.Simulation.SimulationUtilities.Parameters import SimulationParameters
from DymolaSimulation.Simulation.Simulator import DymolaSimulator

if __name__ == "__main__":
    # Set package path - adapt this if necessary
    package_path = os.path.join("D:\\","Dymola","Libary","BuildingSystems", "BuildingSystems")

    # Simulation Parameters
    simulation_parameters = SimulationParameters(algorithm="Dassl",
                                                 start_time=0,
                                                 # stop_time=2.8854e+07,
                                                 stop_time=365 * 3600 * 24,
                                                 output_interval=3600)

    # Parameter Definitions
    package_name = "BuildingSystems.Technologies.Photovoltaics.Examples"
    model_name = "PVModuleSimple"
    output_file_name = "pvmodule"

    # ################ Simulation ############################################################

    # Optional: Dymola Path
    dymolapath = os.environ.get("DYMOLAPATH")

    simulator = DymolaSimulator(workdir_path=package_path,
                                package_paths_full=[os.path.join(package_path,"package.mo")],
                                package_name=package_name,
                                model_name=model_name,
                                result_root_dir=os.path.abspath(package_path),
                                sim_params=simulation_parameters,
                                result_filename=output_file_name,
                                dymolapath=dymolapath)

    # Variables to plot
    plotting_variables = ["pvField.TAmb","pvField.radiationPort.IrrDir","pvField.radiationPort.IrrDif", "pvField.PField"]
    resultfile_path = os.path.join(simulator.get_data_dir(), output_file_name)

    # Create commands and simulate
    simulator.setup_experiment()
    # Adapt parameters
    results = simulator.run_experiment("test", trajectory_names=plotting_variables)
    simulator.terminate()
    simulator.plot_simulation_results(results[["pvField.PField"]])
