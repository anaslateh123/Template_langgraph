from ..models.states.state import State
from ..prompts.prompts import EXAMPLE_PROMPT
from langchain.prompts import PromptTemplate
from ..configs.settings import settings

def your_node_name(state: State) -> State:
    """
    A function node
    """
    # ! Define your node logic here
    text_input = state.get("text_input", "")
    # For example, you can use the EXAMPLE_PROMPT to generate an answer
    system_prompt = PromptTemplate.from_template(EXAMPLE_PROMPT)
    # Call your model here to get the answer
    chain = system_prompt | settings.LLM
    # Generate the answer using the model
    result = chain({"text_input": text_input})
    
    # Return the answer
    return {"answer": result["content"]}