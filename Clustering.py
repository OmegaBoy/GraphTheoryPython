#%%
import networkx as nx
import matplotlib.pyplot as plt
import pylab
  
g = nx.Graph()

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(1, 5)

g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)

g.add_edge(3, 4)
g.add_edge(3, 5)

g.add_edge(4, 5)
  
nx.draw(g, with_labels = True)
pylab.show()
degrees = [val for (node, val) in g.degree()]
print(nx.clustering(g))
# %%