from typing import Optional

from matplotlib import pyplot as plt
import networkx as nx

from graph_merging import merge_graphs
from subgraph import make_subgraph_list


def make_diagram(text: str) -> nx.DiGraph:
    return merge_graphs(make_subgraph_list(text))


def draw_diagram(digraph: nx.DiGraph, pos: Optional[dict] = None) -> None:
    _draw_helper(digraph, pos)
    plt.show()


def save_diagram_image(digraph: nx.DiGraph, filepath: str, pos: Optional[dict] = None) -> None:
    _draw_helper(digraph, pos)
    plt.savefig(filepath)


def _draw_helper(digraph: nx.DiGraph, pos: Optional[dict] = None) -> None:
    pos = pos or nx.spring_layout(digraph)
    edge_labels = _get_edge_labels(digraph)
    nx.draw_networkx(digraph, pos=pos)
    nx.draw_networkx_edge_labels(digraph, pos=pos, edge_labels=edge_labels)


def _get_edge_labels(digraph: nx.DiGraph) -> dict:
    return {
        (v1, v2): '+' if w['weight'] == 1 else '-' for v1, v2, w in nx.convert.to_edgelist(digraph)
    }
