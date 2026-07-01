from griptape_nodes.exe_types.node_types import DataNode
from griptape_nodes.exe_types.param_types.parameter_string import ParameterString

class DummyTextNode(DataNode):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
        self.add_parameter(
            ParameterString(
                name="text_output",
                tooltip="Displays some hardcoded text",
                output_type="str",
                allow_input=False,
                allow_output=True,
                allow_property=False,
                multiline=True,
                markdown=True,
            )
        )
    
    def process(self) -> None:
        self.parameter_output_values["text_output"] = "This is some hardcoded text from the Dummy Text Node."
