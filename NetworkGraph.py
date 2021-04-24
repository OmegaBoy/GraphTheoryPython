#%%
import networkx as nx
import matplotlib.pyplot as plt
import pylab

G = nx.MultiDiGraph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)

G.add_edge(1, 2)
G.add_edge(1, 7)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 7)
G.add_edge(3, 7)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)

pos = nx.random_layout(G)

nx.draw_networkx_nodes(G, pos, node_color = 'r', node_size = 400, alpha = 1)
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
                shrinkA=10, 
                shrinkB=10,
                patchA=None, 
                patchB=None,
                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])),
            ),
        )

for n in G.nodes:
    ax.annotate(
        n, 
        xy=pos[n] - 0.005, 
        xycoords='data',
        )

plt.axis('off')
plt.show()
# %%
