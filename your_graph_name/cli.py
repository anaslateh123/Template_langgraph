"""Command line interface for the LangGraph agent template."""
import click
from your_graph_name import YourGraphName


@click.command()
@click.option('--graph-name', default='my_graph', help='Name of the graph to create')
@click.option('--input-text', default='Hello, world!', help='Input text for the graph')
def main(graph_name: str, input_text: str):
    """Run the LangGraph agent with the specified input."""
    click.echo(f"Creating graph: {graph_name}")
    
    graph = YourGraphName(graph_name)
    compiled_graph = graph.create_graph()
    
    click.echo(f"Running graph with input: {input_text}")
    
    # This is a placeholder - replace with actual graph invocation
    result = {"output": f"Processed: {input_text}"}
    
    click.echo(f"Result: {result}")


if __name__ == '__main__':
    main()
