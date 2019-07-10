from util import *



def MBSAS(x_list, t_hold, maxNumClass):
    cluster = []
    cluster.append([x_list[0]])
    x_list = x_list[1:]
    unClassified = []
    while len(x_list) != 0:
        min_dis, idx_cluster = min_distance(cluster, x_list)
        if min_dis > t_hold and len(cluster) < maxNumClass:
            cluster.append([x_list[0]])
            x_list = x_list[1:]
        else:
            unClassified.append(x_list[0])
            x_list = x_list[1:]

    for i in unClassified:
        min_dis, idx_cluster = closest_cluster(cluster, i)
        cluster[idx_cluster].append(i)

    return cluster
