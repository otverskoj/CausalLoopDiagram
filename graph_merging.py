from math import degrees
import networkx as nx

from merge_rule import MergeRule
from similarity import is_similar


def merge_graphs(graphs: list[nx.DiGraph], 
                 rule: MergeRule = MergeRule.SEQUENCE_MATHCER) -> nx.DiGraph:
    result_graph = graphs[0]
    for graph in graphs[1:]:
        result_graph = _merge_helper(result_graph, graph, rule)
    return result_graph


def _merge_helper(first_graph: nx.DiGraph, second_graph: nx.DiGraph, 
                  rule: MergeRule) -> nx.DiGraph:
    result_edgelist = []
    start_nodes = [node for node, degree in first_graph.out_degree() if degree > 0]
    end_nodes = [node for node, degree in first_graph.out_degree() if degree > 0]
    for start_node in start_nodes:
        for end_node in end_nodes:
            if is_similar(start_node, end_node, rule):
                result_edgelist.extend([
                    (start_node, node, {'weight': weight}) 
                    for _, node, weight in second_graph.out_edges(end_node, data='weight')
                ])
    first_graph.add_edges_from(result_edgelist)
    return first_graph
