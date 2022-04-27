import csv
import numpy as np

def main():
    kernel_hierarchical=[]
    cluster_hierarchical=[]
    kernel_kmeans=[]
    cluster_kmeans=[]
    f_hier = np.zeros([2,2])
    f_kmeans = np.zeros([2,2])

    with open('heirarchical.csv', newline='') as csvfile:
        csvReader = csv.DictReader(csvfile)
        for row in csvReader:
            kernel_hierarchical.append(row['Kernel'])
            cluster_hierarchical.append(row['Cluster'])

    with open('k_means.csv', newline='') as csvfile:
        csvReader = csv.DictReader(csvfile)
        for row in csvReader:
            kernel_kmeans.append(row['Kernel'])
            cluster_kmeans.append(row['Cluster'])

    kernel_kmeans = kernel_kmeans[2:len(kernel_kmeans)]
    kernel_hierarchical= kernel_hierarchical[2:len(kernel_hierarchical)]
    cluster_kmeans = cluster_kmeans[2:len(cluster_kmeans)]
    cluster_hierarchical = cluster_hierarchical[2:len(cluster_hierarchical)]

    for i in range(0, len(kernel_kmeans)):
        for j in range(i+1, len(kernel_kmeans)):
            if kernel_kmeans[i] == kernel_kmeans[j] and (cluster_kmeans[i] == cluster_kmeans[j]):
                f_kmeans[1,1] = f_kmeans[1,1] + 1
            elif kernel_kmeans[i] != kernel_kmeans[j] and cluster_kmeans[i] != cluster_kmeans[j]:
                f_kmeans[0,0] = f_kmeans[0,0] + 1
            elif kernel_kmeans[i] == kernel_kmeans[j] and cluster_kmeans[i] != cluster_kmeans[j]:
                f_kmeans[1,0] = f_kmeans[1,0] + 1
            elif kernel_kmeans[i] != kernel_kmeans[j] and cluster_kmeans[i] == cluster_kmeans[j]:
                f_kmeans[0,1] = f_kmeans[0,1] + 1
            else:
                print("Unclassified - KMeans")

    for i in range(0, len(kernel_hierarchical)):
        for j in range(i+1, len(kernel_hierarchical)):
            if kernel_hierarchical[i] == kernel_hierarchical[j] and cluster_hierarchical[i] == cluster_hierarchical[j]:
                f_hier[1, 1] = f_hier[1, 1] + 1
            elif kernel_hierarchical[i] != kernel_hierarchical[j] and cluster_hierarchical[i] != cluster_hierarchical[j]:
                f_hier[0, 0] = f_hier[0, 0] + 1
            elif kernel_hierarchical[i] == kernel_hierarchical[j] and cluster_hierarchical[i] != cluster_hierarchical[j]:
                f_hier[1, 0] = f_hier[1, 0] + 1
            elif kernel_hierarchical[i] != kernel_hierarchical[j] and cluster_hierarchical[i] == cluster_hierarchical[j]:
                f_hier[0, 1] = f_hier[0, 1] + 1
            else:
                print("Unclassified - Hierarchical")

    print("K-means Rand Statistic and Jaccard Coeff are: ", (f_kmeans[0,0]+f_kmeans[1,1])/np.sum(f_kmeans), " and ",
          (f_kmeans[1,1])/np.sum(f_kmeans))
    print("Hierarchical Rand Statistic and Jaccard Coeff are: ", (f_hier[0, 0] + f_hier[1, 1]) / np.sum(f_hier),
          " and ", (f_hier[1, 1]) / np.sum(f_hier))


if __name__ == '__main__':
    main()
