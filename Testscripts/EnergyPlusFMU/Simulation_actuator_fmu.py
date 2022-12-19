#### The features and the columns should be changed according to the used ones in the FMU, TODO: load them from the files
from DymolaSimulation.Simulation.SimulationUtilities.Parameters import SimulationParameters
from DymolaSimulation.Simulation.Simulator.fmpySimulator import FMPYSimulator
from DymolaSimulation.Simulation.SimulationUtilities import simulation_utils as simutils

if __name__ == "__main__":
    # The path to the FMU must be specified here.
    fmu_filename = "../../EnergyPlusTemplates/FMU/_fmu_export_actuator.fmu"

    # The input and output feature names should be specified here.
    input_feature_names = ["yShade"]
    output_feature_names = ["TRoo"]

    # Define simulation parameters: start time, stop time and output interval
    start_time = 0
    output_interval = 1728000
    num_intervals = 20
    stop_time = start_time + num_intervals * output_interval

    # Create example parameter
    param_vals = {"yShade": 0}
    input_data = simutils.create_input_array(param_vals, num_intervals)

    # Define simulation parameters
    simulation_parameters = SimulationParameters(start_time=start_time,
                                                 stop_time=stop_time,
                                                 output_interval=output_interval,
                                                 num_intervals=num_intervals)

    # Define initial values for output variables
    init_vars = {"TRoo": 25}

    # Instantiate Simulator
    simulator = FMPYSimulator(input_feature_names=input_feature_names,
                              output_feature_names=output_feature_names,
                              fmu_filename=fmu_filename,
                              sim_params=simulation_parameters,
                              result_root_dir="./Results",
                              init_vals=init_vars)

    # Run experiment - store results to CSV
    simulation_results = simulator.run_experiment("Exp1", trajectory_names=output_feature_names, store_csv=True)

    # Plot results
    simulator.plot_simulation_results(simulation_results, out_file_name=f"simulation_results.png")
