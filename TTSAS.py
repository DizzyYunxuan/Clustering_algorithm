from util import *


def TTSAS(x_list, t_hold1, t_hold2, maxNumClass):
    cluster = []
    cluster.append([x_list[0]])
    x_list = x_list[1:]
    unClassified = []
    while len(x_list) != 0:
        min_dis, idx_cluster = min_distance(cluster, x_list)
        if min_dis > t_hold2 and len(cluster) < maxNumClass:
            cluster.append([x_list[0]])
            x_list = x_list[1:]
        elif min_dis < t_hold1:
            cluster[idx_cluster].append(x_list[0])
            x_list = x_list[1:]
        else:
            unClassified.append(x_list[0])
            x_list = x_list[1:]

    while len(unClassified) != 0:
        min_dis, idx_cluster = min_distance(cluster, unClassified)
        cluster[idx_cluster].append(unClassified[0])
        unClassified = unClassified[1:]

    return cluster
