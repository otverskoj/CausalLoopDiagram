import networkx as nx
from causal_loop_diagram import make_diagram, draw_diagram


text: str = "Inflation increases costs. Inflation reduces wages."
diagram: nx.DiGraph = make_diagram(text)
draw_diagram(diagram)
