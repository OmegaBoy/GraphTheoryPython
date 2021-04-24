#%%
import numpy as np
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
g.add_node(7)
g.add_edge(1, 2)
g.add_edge(1, 7)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 7)
g.add_edge(3, 7)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 6)
  
nx.draw(g, with_labels = True)
pylab.show()
degrees = [val for (node, val) in g.degree()]
clustering = nx.clustering(g)
print(clustering)
print("Average Clustering: " + str(sum(dict(clustering).values())/g.number_of_nodes()))
print("Diameter: " + str(nx.diameter(g)))
plt.hist(dict(clustering).values())
print("Adjacency Matrix: " + str(nx.adjacency_matrix(g).todense()))
print("Cliques: " + str(list(nx.enumerate_all_cliques(g))))
print("Simple Paths: " + str(list(nx.all_simple_paths(g,1,4))))
# %%