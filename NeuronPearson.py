# %%
import math
import random
import numpy as np
import matplotlib.pyplot as plt

a = 15
V1  = np.random.uniform(low=0, high=1, size=(10,))
V2 = V1+a*(V1**2)

plt.plot(V1)
plt.plot(V2)

f = np.vstack((V1,V2))

rho = np.corrcoef(f)
corr_matrix = np.corrcoef(f).round(decimals=2)
fig, ax = plt.subplots()
im = ax.imshow(corr_matrix)
im.set_clim(-1, 1)
ax.grid(False)
ax.xaxis.set(
    ticks=(0, 1), 
    ticklabels=('V1', 'V2'))
ax.yaxis.set(
    ticks=(0, 1), 
    ticklabels=('V1', 'V2'))
for i in range(2):
    for j in range(2):
        ax.text(j, i, corr_matrix[i, j], ha='center', va='center', color='r', fontsize=6)
cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
plt.show()
# %%
