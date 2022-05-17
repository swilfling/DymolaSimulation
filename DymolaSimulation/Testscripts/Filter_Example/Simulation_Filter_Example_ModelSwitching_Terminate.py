import os
from DymolaSimulation.SimulationUtilities.Parameters import SimulationParameters, InitializationParameters, DymolaModelParameters
from DymolaSimulation.Simulation.DymolaSimulator import DymolaSimulator
from DymolaSimulation.ComponentExchange.component_exchange import ComponentExchange


if __name__ == "__main__":
    package_path = os.path.abspath("../../DymolaTemplates/DymolaExamples")

    # Simulation Parameters
    simulation_parameters = SimulationParameters(algorithm="Dassl",
                                                 start_time=0,
                                                 stop_time=2,
                                                 num_intervals=200)

    # Parameter Definitions
    package_name = "DymolaExamples.Examples_Filters"
    model_name = "Test_Model_Filters_ModelSwitching_Terminate"
    output_file_name = "result_filters"

    # ################ Simulation ############################################################

    # Optional: Dymola Path
    dymolapath = os.environ.get("DYMOLAPATH")

    # Settings: Extract end values to set start values
    init_variables = {"y_start": 0}

    initialization_parameters = InitializationParameters(use_init_values=True, init_variables=init_variables)
    result_root_dir = os.path.join(package_path, "Filter_Example_ModelSwitching_Terminate")
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
    # FMU Settings
    fmu_instance_name = "UUT"
    plotting_variables = [f"{fmu_instance_name}.u1", f"{fmu_instance_name}.y1"]
    fmu_dir = os.path.join(package_path, "FMUOutput")


    fmu_names = ["Chebyshev", "Butterworth"]
    # Create model definitions
    dymola_models = [DymolaModelParameters(fmu_path=os.path.join(package_path,"FMUOutput", f"{model_type}.fmu"),
                                           model_name=f"{model_type}_fmu",
                                           parameters={"y_start": "y_start"},
                                           is_fmu=True,
                                           use_fmi_init_params=True,
                                           is_exchange_model=True) for model_type in fmu_names]
    # Add terminator
    dymola_models.append(DymolaModelParameters(model_name="TestbenchComponents.ThresholdTerminator",
        package_paths=["../../DymolaTemplates/TestbenchComponents/package.mo"]))
    # Set first model as initial
    dymola_models[0].set_as_exchg_init_model()

    init_mapping = {"y_start": "UUT.y1"}

    exchg = ComponentExchange(simulator, dymola_models, time_delta=0.01)
    list_simulation_results = exchg.run_exchange(list_sim_params=[simulation_parameters], plot_vars=plotting_variables,
                                                       init_mapping=init_mapping)

    simulator.plot_multiple_results(list_simulation_results)
    # Switch back to original
    simulator.terminate()
