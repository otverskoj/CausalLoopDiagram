import networkx as nx

from merge_rule import MergeRule


def merge_graphs(graphs: list[nx.DiGraph], 
                 rule: MergeRule = MergeRule.LEVENSHTEIN) -> nx.DiGraph:
    for i in range(len(graphs) - 1):
        graph = _merge_helper(graphs[i], graphs[i + 1], rule)
    return graph


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


# TODO: Implement similarity calculating for two graph nodes by specific rule 
def is_similar(first_node: str, second_node: str, rule: MergeRule) -> bool:
    return True


def find_end_nodes_with_weights(node: str, edgelist: list[tuple[str, str, int]]) -> list[str]:
    return [
        (edge[1], edge[2]) for edge in edgelist if edge[0] == node
    ]
