#%%
import networkx as nx
import matplotlib.pyplot as plt
import pylab
  
g = nx.Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

g.add_edge(1, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 6)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(4, 5)
g.add_edge(6, 5)
  
nx.draw_circular(g, with_labels = True)
nx.degree_centrality(g)
# %%