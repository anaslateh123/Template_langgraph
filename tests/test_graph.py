"""Test graph functionality."""
import pytest
from your_graph_name import YourGraphName


def test_graph_creation():
    """Test graph creation."""
    graph = YourGraphName("test_graph")
    assert graph.graph_name == "test_graph"
    
    
def test_graph_compilation():
    """Test graph compilation."""
    graph = YourGraphName("test_graph")
    compiled_graph = graph.create_graph()
    assert compiled_graph is not None


def test_graph_exists():
    """Test that YourGraphName class exists and is importable."""
    assert YourGraphName is not None
