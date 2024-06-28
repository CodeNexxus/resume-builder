import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
from matplotlib import pyplot as plt


def escape_label(label):
    return f'"{label}"' if ":" in label else label


def add_to_graph(graph, node, parent=None):
    if node is not None:
        # Escape the label before adding it to the graph
        escaped_label = escape_label(node.value)
        graph.add_node(node.number, label=escaped_label)
        if parent is not None:
            graph.add_edge(parent.number, node.number)
        for child in node.children:
            add_to_graph(graph, child, node)


def transform_ast_to_networkx(ast_root_node):
    graph = nx.DiGraph()
    add_to_graph(graph, ast_root_node)
    return graph


def show_ast(ast_root_node):
    graph = transform_ast_to_networkx(ast_root_node)
    pos = graphviz_layout(graph, prog="dot")
    nx.draw(graph, pos, node_size=500, labels=nx.get_node_attributes(graph, "label"), alpha=0.5, node_color="red",
            with_labels=True)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()
