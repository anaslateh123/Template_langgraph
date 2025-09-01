from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
from .models.states.state import State
from .nodes.your_node_name import your_node_name
from .configs.settings import settings

# ! DEFINE YOUR GRAPH NAME CLASS
class YourGraphName(CompiledStateGraph):
    """
    A class to represent the state graph of your project.
    """
    def __init__(self, graph_name: str):
        super().__init__()
        self.graph_name = graph_name
        self.compiled_graph = None
    
    def _build_graph(self):
        """
        Build the state graph.
        """
        workflow = StateGraph(State, input=State)
        # ! Define your nodes here
        workflow.add_node("your_node_name", your_node_name)
        
        # ! Define the edges between nodes
        workflow.add_edge(START, "your_node_name")
        workflow.add_edge("your_node_name", END)

        if settings.MEMORY_DB_CONNECTION_STRING:
            from langgraph.checkpoint.postgres import PostgresSaver
            with PostgresSaver.from_conn_string(
                settings.MEMORY_DB_CONNECTION_STRING,
            ) as checkpointer:
                self.compiled_graph = workflow.compile(checkpointer=checkpointer, name=self.graph_name)
        else:
            self.compiled_graph = workflow.compile(name=self.graph_name)
        
    def create_graph(self):
        """
        Create the graph.
        """
        if self.compiled_graph is None:
            self._build_graph()
        return self.compiled_graph