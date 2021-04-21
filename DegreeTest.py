#%%
import os
import sys

sys.path.append("./classes")

from SimpleGraphTools import Graph
from SimpleGraphTools import Graph2

g = { "a" : {"d", "f"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {"d"}
    }

graph = Graph2(g)
graph.degree_sequence()
# %%