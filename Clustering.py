#%%
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pylab
  
G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)
G.add_edge(1, 3)
G.add_edge(1, 9)
G.add_edge(2, 4)
G.add_edge(3, 5)
G.add_edge(4, 6)
G.add_edge(5, 7)
G.add_edge(6, 8)
G.add_edge(7, 9)
G.add_edge(8, 10)
G.add_edge(9, 1)
G.add_edge(10, 2)
  
nx.draw(g, with_labels = True)
pylab.show()
degrees = [val for (node, val) in G.degree()]
clustering = nx.clustering(G)
print(clustering)
print("Average Clustering: " + str(sum(dict(clustering).values())/G.number_of_nodes()))
print("Diameter: " + str(nx.diameter(G)))
plt.hist(dict(clustering).values())
print("Adjacency Matrix: " + str(nx.adjacency_matrix(G).todense()))
print("Cliques: " + str(list(nx.enumerate_all_cliques(G))))
print("Simple Paths: " + str(list(nx.all_simple_paths(G,1,4))))
# %%