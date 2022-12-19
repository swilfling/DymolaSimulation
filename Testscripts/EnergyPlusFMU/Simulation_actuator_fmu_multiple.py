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
    output_interval = 86400
    num_intervals = 200
    stop_time = start_time + num_intervals * output_interval

    # Define simulation parameters
    simulation_parameters = SimulationParameters(start_time=start_time,
                                                 stop_time=stop_time,
                                                 output_interval=output_interval,
                                                 num_intervals=num_intervals)

    init_vars = {"TRoo":25}
    simulator = FMPYSimulator(input_feature_names=input_feature_names,
                              output_feature_names=output_feature_names,
                              fmu_filename=fmu_filename,
                              sim_params=simulation_parameters,
                              result_root_dir="./Results",
                              init_vals=init_vars)


    # Create example parameter - multiple parameters
    sweep_vals = [0, 1, 2]
    params_set = [{"yShade": val} for val in sweep_vals]

    # Run experiments for different parameters
    for param_vals in params_set:
        current_sweep_val = param_vals['yShade']
        print(f"Running experiment for sweep val: {current_sweep_val}")
        # Assign input data to simulator
        input_data = simutils.create_input_array(param_vals, num_intervals)
        simulator.input_data = input_data
        # Run experiment and plot results
        simulation_results = simulator.run_experiment(f"Exp_{current_sweep_val}", trajectory_names=output_feature_names, store_csv=True)
        simulator.plot_simulation_results(simulation_results, out_file_name=f"Exp_{current_sweep_val}.png")
