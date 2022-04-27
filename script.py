import numpy as np
import math

max_rows = 0
max_cols = 0

for it in in_data:
    if it.get_class() > max_cols:
        max_cols = int(it.get_class())
    if int(it.metas[0]) > max_rows:
        max_rows = int(it.metas[0])

max_rows = max_rows + 1
max_cols = max_cols + 1

############## Data Table #################
classifier_cluster_matrix = np.zeros([max_rows, max_cols])
for element in in_data:
    classifier_cluster_matrix[int(element.metas[0]), int(element.get_class())] = classifier_cluster_matrix[
                                                                                     int(element.metas[0]), int(
                                                                                         element.get_class())] + 1
N = np.sum(classifier_cluster_matrix)  # total number of elements

##### Entropy vars #######
row_entropy = []
entropy = 0

##### Recall Vars ########
recall = np.zeros(np.shape(classifier_cluster_matrix))

############# Entropy Calculations ############################################################################
for x in classifier_cluster_matrix:
    imm_row_entropy = 0
    for y in x:
        p = y / np.sum(x, axis=0, dtype=float)
        if p == 0:
            continue
        imm_row_entropy = imm_row_entropy + p * math.log2(p)
    row_entropy.append(-imm_row_entropy)

for i in range(0, len(row_entropy)):
    entropy = entropy + np.sum(classifier_cluster_matrix[i]) * (row_entropy[i] / N)
##################################################################################################################

############# Recall Calculations ################################################################################
for i in range(0, len(classifier_cluster_matrix)):
    for j in range(0, len(classifier_cluster_matrix[i])):
        recall[i, j] = classifier_cluster_matrix[i, j] / np.sum(classifier_cluster_matrix[:, j])
##################################################################################################################

print("The Entropy is", entropy)
print("The recall matrix is\n", recall)

############# Populate F Matrix ##################################################################################
f_matrix = np.zeros([2, 2])
for i in range(0, len(in_data)):
    for j in range(i + 1, len(in_data)):
        if in_data[i].get_class() == in_data[j].get_class() and in_data[i].metas[0] == in_data[j].metas[0]:
            f_matrix[1, 1] = f_matrix[1, 1] + 1
        elif in_data[i].get_class() != in_data[j].get_class() and in_data[i].metas[0] != in_data[j].metas[0]:
            f_matrix[0, 0] = f_matrix[0, 0] + 1
        elif in_data[i].get_class() == in_data[j].get_class() and in_data[i].metas[0] != in_data[j].metas[0]:
            f_matrix[1, 0] = f_matrix[1, 0] + 1
        elif in_data[i].get_class() != in_data[j].get_class() and in_data[i].metas[0] == in_data[j].metas[0]:
            f_matrix[0, 1] = f_matrix[0, 1] + 1

print("\nThe f matrix:\n", f_matrix)
print("The Rand Statistic and Jaccard Coeff are:", (f_matrix[0, 0] + f_matrix[1, 1]) / np.sum(f_matrix), ",",
      (f_matrix[1, 1]) / np.sum(f_matrix))

##################################################################################################################