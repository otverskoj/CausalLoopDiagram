from typing import Iterable
from matplotlib import pyplot as plt
import networkx as nx

from verbs import VERBS_INCREASE


def make_subgraph_list(graph_data: list[dict]) -> list[nx.DiGraph]:
    return [
        make_subgraph(item)
        for item in graph_data
    ]


def make_subgraph(graph_data: dict) -> nx.DiGraph:
    return nx.DiGraph(convert_to_edgelist(graph_data))


def convert_to_edgelist(raw_data: dict) -> list[tuple[str, str, dict[str, int]]]:
    return [(
        raw_data['data']['subject'], raw_data['data']['object'], 
        {
            'weight': get_verb_weight(raw_data['data']['predicate'])
        }
    )]


def get_verb_weight(verb: str) -> int:
    return 1 if verb in VERBS_INCREASE else -1


def draw_digraph_with_edge_labels(digraph, pos=None):
    pos = pos or nx.spring_layout(digraph)
    edge_labels = {
        (v1, v2): '+' if w['weight'] == 1 else '-' for v1, v2, w in nx.convert.to_edgelist(digraph)
    }
    nx.draw_networkx(digraph, pos=pos)
    nx.draw_networkx_edge_labels(digraph, pos=pos, edge_labels=edge_labels)
    plt.show()
