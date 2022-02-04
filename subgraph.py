from matplotlib import pyplot as plt
import networkx as nx

from verbs import VERBS_INCREASE
from dependency_parser import parse_dependencies


def draw_digraph_with_edge_labels(digraph, pos=None):
    pos = pos or nx.spring_layout(digraph)
    edge_labels = {
        (v1, v2): '+' if w['weight'] == 1 else '-' for v1, v2, w in nx.convert.to_edgelist(digraph)
    }
    nx.draw_networkx(digraph, pos=pos)
    nx.draw_networkx_edge_labels(digraph, pos=pos, edge_labels=edge_labels)
    plt.show()


def convert_to_edgelist(raw_data: list[dict]) -> list[tuple[str, str, dict[str, int]]]:
    return [
        (d['data']['subject'], d['data']['object'], 
        {'weight': get_verb_weight(d['data']['predicate'])})
        for d in raw_data
    ]


def get_verb_weight(verb: str) -> int:
    return 1 if verb in VERBS_INCREASE else -1


graph_data = parse_dependencies("Inflation increases costs. Inflation reduces wages.")
directed_graph = nx.DiGraph(convert_to_edgelist(graph_data))
draw_digraph_with_edge_labels(directed_graph)
