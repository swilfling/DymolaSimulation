from ..SimulationUtilities import DymolaCommands


def get_df_end_values(df, labels):
    return [df[name][-1] for name in labels] if df is not None else []


def get_final_time(df):
    return df.index[-1].total_seconds() if df is not None else 0


def get_start_vals(df, mapping, default_init=0):
    if df is None:
        return {val_name: default_init for val_name in mapping}
    else:
        return {val_name: (df[traj_name].iloc[-1] if traj_name else default_init) for val_name, traj_name in mapping.items()}


def early_termination(terminate_time, time_delta, stepsize, stop_time):
    return terminate_time + time_delta + stepsize < stop_time


def calc_num_intervals(start_time, stop_time, stepsize):
    return int((stop_time - start_time)/stepsize)


def switch_components(simulator, component_1, component_2):
    switch_model_commands = DymolaCommands.create_model_switch_cmds(simulator.package_name, simulator.model_name, component_1, component_2, component_1.instance_name)
    simulator.execute_commands(switch_model_commands, f"model_switching_script_{component_1.model_name }_{component_2.model_name}.mos")


def create_FMI_init_variables(simulation_parameters):
    return {"fmi_StartTime": simulation_parameters.start_time,
            "fmi_StopTime": simulation_parameters.stop_time,
            "fmi_NumberOfSteps": simulation_parameters.num_intervals}