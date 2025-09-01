from typing_extensions import TypedDict, Annotated

class StructuredOutput(TypedDict):
    """
    DEFINE YOUR Structure HERE.
    """
    # ! Define the attributes of your structure here
    name: Annotated[str, "name of the user"]