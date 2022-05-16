from dataclasses import dataclass, field
from .parameters import Parameters

@dataclass
class InitializationParameters(Parameters):
    use_init_values: bool = False
    init_variables: dict = field(default_factory=dict)
    use_init_file: bool = False
    init_filename: str = ""

    def set_initialization_parameters_full(self, init_file, init_variables):
        self.init_variables.update(init_variables)
        self.use_init_file = True
        self.init_filename = init_file
        self.use_init_values = True


