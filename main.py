import networkx as nx
from causal_loop_diagram import deserialize, make_diagram, draw_diagram, serialize, to_python_dict


text: str = "Inflation increases costs. Inflation reduces wages."
diagram: nx.DiGraph = make_diagram(text)
