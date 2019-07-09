import numpy as np
from BSAS import *
from MBSAS import *
from TTSAS import *

def mean_center(cluster_elements):
    res = 0
    cluster_elements = np.array(cluster_elements)
    for i in cluster_elements:
        res += i
    # print(len(cluster_elements))
    res = res / len(cluster_elements)
    return list(res)


def dis_cal(center, x):
    center, x = np.array(center), np.array(x)
    return np.sum((center - x) ** 2) ** (1 / 2)


def min_distance(clusters, x_list):
    min_dis = float('inf')
    closest_cluster = 0
    # min_dis_arg = 0
    for i in range(len(clusters)):
        center = mean_center(clusters[i])
        dis = dis_cal(center, x_list[0])
        if dis < min_dis:
            min_dis = dis
            closest_cluster = i
            # min_dis_arg = j

    return min_dis, closest_cluster


def closest_cluster(clusters, x):
    min_dis = float('inf')
    closest_cluster = 0
    # min_dis_arg = 0
    for i in range(len(clusters)):
        center = mean_center(clusters[i])
        dis = dis_cal(center, x)
        if dis < min_dis:
            min_dis = dis
            closest_cluster = i
            # min_dis_arg = j

    return min_dis, closest_cluster


if __name__ == '__main__':
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 = [1, 1], [1, 2], [2, 2], [2, 3], [3, 3], [3, 4], \
                                                                  [4, 4], [4, 5], [5, 5], [5, 6], [-4, 5], [-3, 5], \
                                                                  [-4, 4], [-3, 4]

    # Different order may cause different results
    # questionA
    # x_list = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14]

    # questionB
    x_list = [x1, x10, x2, x3, x4, x11, x12, x5, x6, x7, x13, x8, x14, x9]

    # questionC
    # x_list = [x1, x10, x5, x2, x3, x11, x12, x4, x6, x7, x13, x14, x8, x9]

    # Args
    maxNumClass = 14
    t_hold = 2 ** (1 / 2)
    t_hold1 = 2 ** (1 / 2)
    t_hold2 = 2

    # 3 methods
    res1 = BSAS(x_list, t_hold, maxNumClass)
    res2 = MBSAS(x_list, t_hold, maxNumClass)
    res3 = TTSAS(x_list, t_hold1, t_hold2, maxNumClass)

    for i in res1:
        print(i)
