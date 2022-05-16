from dataclasses import dataclass
from .parameters import Parameters

@dataclass
class SimulationParameters(Parameters):
    algorithm: str = "Dassl"
    start_time: float = 0.0
    stop_time: float = 0.0
    num_intervals: int = 0
    output_interval: float = 0
    tolerance: float = 0.0001
    fixed_stepsize: float = 0.0

    @staticmethod
    def create_simulation_parameters(num_experiments,start_time, start_duration=0, experiment_duration=0, timestep=900):
        simulation_parameters_list = [SimulationParameters(start_time=start_time, stop_time=start_time + start_duration,
                                                           num_intervals=int(start_duration / timestep), output_interval=timestep)]
        for i in range(num_experiments):
            simulation_parameters_list.append(SimulationParameters(start_time=start_time + start_duration + i * experiment_duration,
                                                                   stop_time=start_time + start_duration + (i+1) * experiment_duration,
                                                                   num_intervals=int(experiment_duration/timestep), output_interval=timestep))
        return simulation_parameters_list

