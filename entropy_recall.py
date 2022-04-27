import numpy as np
import math

############## Data Table #################
k_means = np.array([[64, 2, 8],
                  [5,68,0],
                  [1, 0, 62]])

hierarchical = np.array([[4, 68, 0],
                  [2,0,60],
                  [64, 2, 10]])
N = np.sum(k_means) # total number of elements

##### Entropy vars #######
entropy_kmeans = []
entropy_hierarchical = []
entropy_hierarchical_sum = 0
entropy_kmeans_sum = 0

##### Recall Vars ########
recall_kmeans = np.zeros(np.shape(k_means))
recall_hierarchical = np.zeros(np.shape(k_means))

############# Entropy Calculations ############################################################################
for x in k_means:
    row_entropy = 0
    for y in x:
        p = y / np.sum(x, axis=0, dtype=float)
        if p == 0:
            continue
        row_entropy = row_entropy + p * math.log2(p)
    entropy_kmeans.append(-row_entropy)

for x in hierarchical:
    row_entropy = 0
    for y in x:
        p = y / np.sum(x, axis=0, dtype=float)
        if p == 0:
            continue
        row_entropy = row_entropy + p * math.log2(p)
    entropy_hierarchical.append(-row_entropy)

for i in range(0,3):
    entropy_hierarchical_sum = entropy_hierarchical_sum + np.sum(hierarchical[i])*entropy_hierarchical[i]/N
    entropy_kmeans_sum = entropy_kmeans_sum + np.sum(k_means[i])*entropy_kmeans[i]/N
##################################################################################################################

for i in range(0, len(k_means)):
    for j in range(0, len(k_means[i])):
        recall_kmeans[i,j] = k_means[i,j]/np.sum(k_means[:,j])
        recall_hierarchical[i,j] = hierarchical[i,j]/np.sum(hierarchical[:,j])

print("End")