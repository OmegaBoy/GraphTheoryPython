#%%
import matplotlib.pyplot as plt
import numpy as np
from networkx import nx

i = 1000
N = 50
distP = list()
avgDist = list()
avgDegree = list()
avgClt = list()
for p in range(i):
    G = nx.erdos_renyi_graph(N, p/i)
    try:
        avgDist.append(nx.average_shortest_path_length(G))
        degrees = [val for (node, val) in G.degree()]
        avgDegree.append(sum(degrees)/N)
        distP.append(p/i)
        avgClt.append(nx.average_clustering(G))
    except: pass
plt.plot(distP, avgDegree)
plt.show()
plt.plot(distP, avgClt)
plt.show()
plt.plot(distP, avgDist)
plt.show()