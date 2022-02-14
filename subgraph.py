import networkx as nx
from dependency_parser import parse_dependencies
from verbs import VERBS_INCREASE


def make_subgraph_list(text: str) -> list[nx.DiGraph]:
    return [
        _make_subgraph(item)
        for item in parse_dependencies(text)
    ]


def _make_subgraph(graph_data: dict) -> nx.DiGraph:
    return nx.DiGraph(_convert_to_edgelist(graph_data))


def _convert_to_edgelist(raw_data: dict) -> list[tuple[str, str, dict[str, int]]]:
    return [(
        raw_data['data']['subject'], raw_data['data']['object'], 
        {
            'weight': _get_verb_weight(raw_data['data']['predicate'])
        }
    )]


def _get_verb_weight(verb: str) -> int:
    return 1 if verb in VERBS_INCREASE else -1
