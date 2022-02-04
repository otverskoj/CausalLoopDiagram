from dependency_parser import parse_dependencies
from subgraph import make_subgraph_list


graphs = make_subgraph_list(parse_dependencies("Inflation increases costs. Inflation reduces wages."))
print(graphs[0].nodes)
