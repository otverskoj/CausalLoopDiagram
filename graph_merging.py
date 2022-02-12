import networkx as nx

from merge_rule import MergeRule
from similarity import is_similar


def merge_graphs(graphs: list[nx.DiGraph], 
                 rule: MergeRule = MergeRule.LEVENSHTEIN) -> nx.DiGraph:
    result_graph = graphs[0]
    for graph in graphs[1:]:
        result_graph = _merge_helper(result_graph, graph)
    return result_graph


def _merge_helper(graph1: nx.DiGraph, graph2: nx.DiGraph, 
                  rule: MergeRule = MergeRule.LEVENSHTEIN) -> nx.DiGraph:
    graph2_edgelist = nx.convert.to_edgelist(graph2)
    
    result_edgelist = []
    for start_node in graph1.nodes:
        for end_node in graph2.nodes:
            if is_similar(start_node, end_node, rule):
                end_nodes_with_weights = find_end_nodes_with_weights(end_node, graph2_edgelist)
                result_edgelist.extend([
                    (start_node, node, weight) 
                    for node, weight in end_nodes_with_weights
                ])
    return nx.DiGraph(result_edgelist)


def find_end_nodes_with_weights(node: str, edgelist: list[tuple[str, str, int]]) -> list[str]:
    return [
        (edge[1], edge[2]) for edge in edgelist if edge[0] == node
    ]
