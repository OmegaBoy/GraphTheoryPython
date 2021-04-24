# %%
import math
import numpy as np
import matplotlib.pyplot as plt

S1  = [0.99, 1.28, 1.26, 1.6, 01.01, 1.34, 1.36, 0.94, 01.09, 0.5, 0.62, 0.83, 0.01, 0.52, 0.16, -0.05, -0.34, -0.53, -0.45, -0.43, -0.33, -0.47, -0.26, -0.3, -0.29, -0.99, -0.4, -0.17, -0.72, -0.15, -0.17, -0.03, 0.11, -0.22, 0.23, 0.23, 0.6, 0.62, 0.98, 0.94, 0.73, 0.54, 0.68, 1.27, 1.27, 1.36, 1.58, 01.06, 01.09, 1.4, 1.49, 01.07, 1.28, 01.04, 1.22, 1.4, 0.7, 0.73, 0.64, 0.36, 0.22, 0.62, 0.63, 0, 0.49, 0.23, -0.12, 0.1, -0.26, -0.42, -0.39, -0.89, -0.22, -0.56, -0.37, -0.99, -0.62, -0.89, -0.75, -0.56, -0.09, -0.3, 0.03, 0.28, -0.21, 0.54, 0.53, 0.73, 0.49, 0.94, 0.74, 0.54, 0.68, 01.06, 0.97, 1.17, 01.03, 1.74, 1.27]
S2  = [5.1, 5.38, 5.48, 5.49, 5.6, 5.11, 05.04, 4.84, 4.53, 4.55, 4.56, 4.66, 4.16, 4.33, 4.46, 4.34, 3.85, 04.07, 3.63, 3.6, 3.69, 3.77, 3.45, 3.72, 3.35, 03.01, 3.69, 3.83, 3.13, 3.32, 3.87, 3.78, 3.91, 3.87, 4.23, 4.34, 3.95, 4.43, 4.74, 4.91, 4.93, 4.62, 05.02, 4.99, 5.4, 4.98, 5.65, 5.41, 5.77, 5.6, 5.29, 5.73, 5.35, 05.01, 4.89, 5.29, 4.97, 5.11, 4.96, 4.59, 4.22, 4.63, 4.72, 4.24, 4.2, 3.7, 4, 3.54, 04.01, 3.32, 3.66, 3.49, 3.65, 3.23, 3.74, 3.76, 3.12, 3.53, 3.25, 3.24, 3.69, 3.83, 4.17, 4.19, 3.75, 4.1, 4.68, 4.22, 4.67, 4.61, 4.69, 5.27, 5, 4.99, 5.26, 5.25, 05.01, 5.39, 5.42]
S3  = [0.76, 0.83, 0.59, 0.26, 0.72, 0.24, 0.52, 0.28, 0.02, 0.35, 0.29, 0.55, 0, 0.15, 0.56, 0.13, 0.39, 0.09, 0.81, 0.6, 0.99, 0.44, 0.46, 0.54, 0.47, 0.77, 0.09, 0.39, 0.19, 0.99, 0.67, 0.55, 0.74, 0.39, 0.51, 0.4, 0.27, 0.82, 0.28, 0.44, 0.66, 0.52, 0.46, 0.06, 0.68, 0.55, 0.24, 0.01, 0.03, 0.67, 0.22, 0.48, 0.77, 0.37, 0.84, 0.39, 0.47, 0.26, 0.43, 0.29, 0.15, 0.49, 0.44, 0.43, 0.47, 0.04, 0.74, 0.38, 0.93, 0.98, 0.5, 0.32, 0.51, 0.61, 0.68, 0.28 , 0.77, 0.49, 0.06, 0.81, 0.86, 0.75, 0.36, 0.64, 0.14, 0.86, 0.3, 0.13, 0.43, 0.01, 0.69, 0.38, 0.38, 0.51, 0.83, 0.63, 0.67, 0.28, 0.66]
S4  = [1.36, 1, 1.67, 0.91, 1.41, 0.95, 0.89, 1.27, 0.98, 0.72, 0.33, 0.78, 0.27, 0.36, -0.19, -0.27, -0.37, -0.51, 0.02, -0.15, -0.11, -0.35, -0.92, -0.88, -0.35, -0.41, -0.9, -0.71, -0.09, -0.6, -0.22, -0.17, -0.28, -0.07, 0.27, 0.3, 0.45, 0.08, 0.79, 0.31, 0.99, 1.16, 01.05, 1.52, 1.24, 1.64, 1.54, 1.11, 01.06, 1.55, 1.18, 1.47, 0.98, 1.63, 1.1, 1.48, 0.87, 0.84, 0.58, 0.72, 0.8, 0.27, -0.04, 0.14, 0.44,  -0.15, 0.02,  -0.17, -0.38,  -0.35, -0.42, -0.9,  -0.58,  -0.77,  -0.34, -0.31,  -0.89,  -0.77, -0.76,  -0.09,  -0.51, 0.07,  -0.46, 0.29, 0.07, 0.45, 0.05, 0.22, 0.31, 0.69, 0.54, 0.95, 0.76, 1.3, 1.15, 1.63, 1.6, 1.54, 1.25]
S5  = [2.41, 1.98, 2.54, 2.34, 2.14, 1.75, 02.06, 1.5, 1.55, 01.09, 0.5, 0.63, -0.1, -0.07, 0.17, -0.6, -1.05, -1.22, -0.94, -1.01, -1.07, -1.16, -1.37, -1.62, -1.71, -1.73, -1.33, -1.31, -1.56, -1.43, -1.41, -1.01, -0.96, -0.47, -0.04, 0.41, 0.31, 0.25, 0.51, 01.09, 1.28, 1.25, 1.63, 1.89, 1.65, 02.04, 2.42, 2.42, 2.38, 2.61, 2.51, 2.67, 2.21, 2.52, 1.96, 1.94, 1.36, 1.14, 1.62, 1.28, 0.42, 0.69, 0.29, 0.42, -0.07, -0.76, -1.05, -1.14, -1.05, -1.4, -1.28, -1.66, -1.42, -1.42, -1.58, -1.76, -1.58, -1.77, -1.38, -0.88, -0.76, -1, -0.94, -0.15, -0.05, -0.03, -0.04, 0.4, 0.91, 1.13, 01.08, 1.35, 1.88, 2.13, 2.29, 02.08, 2.32, 2.41, 2.68]
S6  = [1.13, 1.23, 01.01, 0.57, 0.06, -0.18, -0.19, -0.44, -0.45, -0.32, -0.49, -0.14, -0.02, 0, 0.33, 0.81, 1.31, 1.1, 1.12, 1.37, 1.18, 1.38, 0.98, 1.1, 0.17, 0.03, -0.08, -0.58, -0.3, -0.92, -0.47, -0.25, -0.16, 0, 0.76, 0.43, 1.32, 1.37, 0.95, 1.41, 1.18, 0.85, 0.71, 0.31, 0.1, 0.36, -0.23, -0.46, -0.34, -0.97, -0.82, -0.79, 0.19, -0.11, 0.26, 0.6, 0.76, 1.18, 01.06, 1.67, 1.37, 1.11, 0.61, 01.08, 0.65, -0.23, -0.43, -0.79, -0.29, -0.57, -0.6, -0.72, -0.03, 0.12, 0.18, 01.07, 0.86, 1.59, 1.26, 1.72, 1.42, 0.96, 0.92, 0.7, 0.19, -0.25, -0.52, -0.35, -0.15, -0.48, -0.42, -0.6, -0.06, -0.12, 0.23, 0.35, 1.11, 1.48, 1.3]
S7  = [-2.94, -2.37, -2.72, -2.12, -1.92, -1.8, -1.7, -0.85, -0.69, -0.6, 0.08, -0.06, 0.94, 0.96, 01.04, 1.38, 1.95, 2.11, 2.73, 3.19, 03.06, 3.43, 3.44, 3.15, 3.8, 3.52, 03.08, 3.41, 2.74, 2.6, 2.37, 02.03, 1.86, 1.5, 1.3, 1.1, 0.4, 0.38, -0.17, -0.87, -0.62, -1.55, -1.68, -1.5, -1.65, -1.85, -2.58, -2.84, -2.23, -2.82, -2.38, -2.43, -2.42, -2.57, -1.86, -1.76, -1.27, -1.42, -0.64, -0.35, 0.18, -0.03, 0.79, 1.24, 1.36, 1.69, 2.14, 2.47, 2.92, 2.99, 2.75, 3.1, 3.23, 3.73, 3.11, 3.38, 3.14, 3.48, 3.34, 03.04, 2.5, 2.51, 1.68, 1.37, 1.24, 0.96, 0.97, 0.16, 0, -0.41, -0.59, -1.37, -1.9, -1.81, -2.28, -2.27, -2, -2.24, -2.24]
S8  = [0.68, 0.01, 0.65, 0.76, 0.88, 0.9, 0.09, 0.05, 0.73, 0.84, 0.03, 0.21, 0.24, 0.15, 0.56, 0.65, 0.14, 0.14, 0.91, 0.63, 0.51, 0.71, 0.68, 0.45, 0.15, 0.68, 0.21, 0.78, 0.4, 0.63, 0.32, 0.16, 0.59, 0.08, 0.94, 0.34, 0.97, 0.44, 0.08, 0.54, 0.37, 0.16, 0.83, 0.03, 0.19, 0.26, 0.67, 0.69, 0.25, 0.22, 0.16, 0.72, 0.33, 0.12, 0.58, 0.46, 0.53, 0.8, 0.95, 0.33, 0.22, 0.23, 0.59, 0.87, 0.57, 0.02, 0.35, 0.76, 0.6, 0.67, 0.5, 0.55, 0.49, 0.24, 0.9, 0.12, 0.76, 0.49, 0.42, 0.17, 0.81, 0.72, 0.67, 0.38, 0.98, 0.48, 0.41, 0.59, 0.4, 0.8, 0.31, 0.83, 0.79, 0.37, 0.36, 0.6, 0.02, 0.66, 0.28]
S9  = [1.49, 1.12, 0.92, 1.1, 0.22, 0.42, 0.17, -0.2, -0.15, -0.78, -0.52, -0.24, -0.44, 0.16, 0.2, 0.81, 1.35, 1.44, 1.15, 1.35, 01.03, 1.4, 0.75, 0.56, 0.5, -0.14, -0.52, -0.47, -0.47, -0.44, -0.39, -0.42, -0.17, -0.01, 0.26, 0.74, 0.79, 1.27, 01.08, 1.31, 1.5, 1.39, 1.14, 0.61, 0.28, -0.11, -0.49, -0.51, -0.66, -0.55, -0.91, -0.41, -0.23, 0.11, 0.7, 0.63, 1.12, 1.2, 01.09, 1.64, 1.11, 1.16, 1.25, 0.56, 0.13, 0.14, -0.53, -0.24, -0.37, -0.92, -0.37, -0.33, -0.2, 0.02, 0.2, 0.64, 0.86, 1.1, 1.28, 1.46, 1.37, 1.51, 01.04, 0.62, 0.5, 0.05, -0.4, -0.46, -0.27, -0.7, -0.84, -0.71, -0.14, -0.27, 0.75, 0.91, 1.32, 1.39, 1.71]
S10 = [-1.24, -1.88, -1.3, -1.46, -1.27, -1.41, -1.22, -0.46, -0.14, -0.29, 0.02, -0.02, 0.38, 01.05, 01.01, 1.49, 1.4, 1.64, 2.15, 2.28, 02.08, 1.87, 2.67, 2.4, 2.49, 2.65, 2.25, 02.09, 1.89, 2.25, 1.55, 1.96, 1.42, 01.05, 0.99, 0.79, 0.8, 0.48, 0.35, -0.45, -0.6, -0.83, -0.81, -1.07, -1.13, -1.41, -1.69, -1.27, -1.37, -1.48, -1.45, -1.89, -1.26, -1.62, -1.01, -1.27, -0.58, -1.07, -0.37, -0.11, -0.3, 0.25, 0.39, 0.49, 1.37, 1.54, 1.18, 1.34, 1.87, 02.06, 1.78, 2.35, 2.51, 2.46, 2.52, 2.55, 2.2, 2.5, 2.27, 1.64, 2.21, 1.33, 1.72, 1.4, 1.16, 0.77, 0.9, 0.17, 0.28, -0.33, -0.37, -0.56, -1.04, -1.4, -1.15, -1.06, -1.7, -1.42, -1.89]

f = np.vstack((S1,S2))
f = np.vstack((f,S3))
f = np.vstack((f,S4))
f = np.vstack((f,S5))
f = np.vstack((f,S6))
f = np.vstack((f,S7))
f = np.vstack((f,S8))
f = np.vstack((f,S9))
f = np.vstack((f,S10))

rho = np.corrcoef(f)
corr_matrix = np.corrcoef(f).round(decimals=2)
fig, ax = plt.subplots()
im = ax.imshow(corr_matrix)
im.set_clim(-1, 1)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ticklabels=('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10'))
ax.yaxis.set(ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ticklabels=('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10'))
for i in range(10):
    for j in range(10):
        ax.text(j, i, corr_matrix[i, j], ha='center', va='center', color='r', fontsize=6)
cbar = ax.figure.colorbar(im, ax=ax, format='% .2f')
plt.show()
# %%