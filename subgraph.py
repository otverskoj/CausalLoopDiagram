from matplotlib import pyplot as plt
import networkx as nx

from verbs import VERBS_INCREASE


# change to import
FAKE_DATA = [
    {
        'data': {'object': 'million', 'predicate': 'be', 'subject': 'income'},
        'sentence': 'Net income was $9.4 million compared to the prior year of $2.7 million.'
    },
    {
        'data': {'object': 'dollars', 'predicate': 'exceed', 'subject': 'Revenue'},
        'sentence': 'Revenue exceeded twelve billion dollars, with a loss of $1b.'
    }
]


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


directed_graph = nx.DiGraph(convert_to_edgelist(FAKE_DATA))
draw_digraph_with_edge_labels(directed_graph)
