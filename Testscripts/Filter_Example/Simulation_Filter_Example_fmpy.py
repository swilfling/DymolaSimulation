#### The features and the columns should be changed according to the used ones in the FMU, TODO: load them from the files
import numpy as np
import numpy.lib.recfunctions as rfs
from DymolaSimulation.Simulation.SimulationUtilities.Parameters import SimulationParameters, InitializationParameters
from DymolaSimulation.Simulation.Simulator.fmpySimulator import FMPYSimulator
import os


if __name__ == "__main__":
    hybridcosim_path = os.environ.get('HYBRIDCOSIM_REPO_PATH')
    data_filename = "../../DymolaTemplates/DymolaExamples/example_data.csv"

    # Get FMU interface
    fmu_filename = "../../DymolaTemplates/DymolaExamples/FMUOutput/Butterworth.fmu"
    input_feature_names = ["u1"]
    output_feature_names = ["y1"]

    input_data = np.genfromtxt(data_filename, delimiter=';', names=True)
    input_data = rfs.rename_fields(input_data, {"Zeitraum": "Time"})
    input_data = input_data[["Time"] + input_feature_names + output_feature_names]
    init_data = input_data[0]

    start_time = 0
    output_interval = 1
    num_intervals = 11
    stop_time = start_time + num_intervals * output_interval
    input_data = input_data[:stop_time+1]

    simulation_parameters = SimulationParameters(start_time=start_time,
                                                 stop_time=stop_time,
                                                 output_interval=output_interval,
                                                 num_intervals=num_intervals)

    init_vars = {name:init_data[i] for i, name in enumerate(output_feature_names)}
    initialization_parameters = InitializationParameters(use_init_values=True, init_variables=init_vars)

    simulator = FMPYSimulator(input_feature_names=input_feature_names,
                              output_feature_names=output_feature_names,
                              fmu_filename=fmu_filename,
                              sim_params=simulation_parameters,
                              initialization_parameters=initialization_parameters,
                              input_data=input_data,
                              result_root_dir="../DymolaPythonInterface/FMPY/")

    simulation_results = simulator.run_experiment("Exp1", trajectory_names=output_feature_names, plot_enabled=True, store_csv=True)

    # Plot each feature separately
    for feature in output_feature_names:
        simulator.plot_simulation_results(simulation_results[[f"data_{feature}",feature]], out_file_name=f"{feature}.png")
