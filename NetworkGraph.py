#%%
import networkx as nx
import matplotlib.pyplot as plt
import pylab
factor = 0.05
G = nx.MultiDiGraph()

N = 100
M = 2
for n in range(N):
    G.add_node(n + 1)

for n in range(N - M):
    G.add_edge(n + 1, n + 1 + M)

for n in range(M):
    G.add_edge(N - (M - (n + 1)), n + 1)

pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G, pos, node_color = 'r', node_size = 400*factor, alpha = 1)
ax = plt.gca()
for e in G.edges:
    ax.annotate(
        "",
        xy=pos[e[0]], 
        xycoords='data',
        xytext=pos[e[1]], 
        textcoords='data',
        arrowprops=dict
            (
                arrowstyle="-", 
                color="0.5",
                shrinkA=10*factor, 
                shrinkB=10*factor,
                patchA=None, 
                patchB=None,
                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])),
            ),
        )

for n in G.nodes:
    ax.annotate(
        n, 
        xy=pos[n] - (0.025*factor), 
        xycoords='data',
        fontsize=10*factor
        )

plt.axis('off')
plt.show()
# %%
