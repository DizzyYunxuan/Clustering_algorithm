import numpy as np


def mean_center(cluster_elements):
    res = 0
    cluster_elements = np.array(cluster_elements)
    for i in cluster_elements:
        res += i
    res = res / len(cluster_elements)
    return list(res)


def dis_cal(center, x):
    center, x = np.array(center), np.array(x)
    return np.sum((center - x) ** 2) ** (1 / 2)


def min_distance(clusters, x_list):
    min_dis = float('inf')
    closest_cluster = 0
    for i in range(len(clusters)):
        center = mean_center(clusters[i])
        dis = dis_cal(center, x_list[0])
        if dis < min_dis:
            min_dis = dis
            closest_cluster = i

    return min_dis, closest_cluster


def closest_cluster(clusters, x):
    min_dis = float('inf')
    closest_cluster = 0
    for i in range(len(clusters)):
        center = mean_center(clusters[i])
        dis = dis_cal(center, x)
        if dis < min_dis:
            min_dis = dis
            closest_cluster = i

    return min_dis, closest_cluster
