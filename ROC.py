#%%
import matplotlib.pyplot as plt
import numpy as np

def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()

# fpr = [ 1, 0.9375, 0.8125, 0.625, 0.375, 0.1875, 0.0625, 0 ]# false_positive_rate
# tpr = [ 1, 1, 1, 1, 0.8888888889, 0.6666666667, 0.3333333333, 0.1111111111 ]# true_positive_rate 

fpr = [ 1, 0.75, 0.5625, 0.375, 0.25, 0.125, 0.0625, 0 ]# false_positive_rate
tpr = [ 1, 1, 1, 1, 1, 0.7777777778, 0.4444444444, 0.1111111111 ]# true_positive_rate 

# This is the ROC curve
plot_roc_curve(fpr, tpr)

# This is the AUC
print(abs(np.trapz(tpr, fpr)))