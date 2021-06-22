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

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)

G.add_edge(2, 3)

G.add_edge(3, 4)
G.add_edge(3, 5)

G.add_edge(4, 5)
  
nx.draw(G, with_labels = True)
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