from clustering import *
import numpy as np


def BSAS(x_list, t_hold, maxNumClass):
    cluster = []
    cluster.append([x_list[0]])
    x_list = x_list[1:]
    while len(x_list) != 0:
        min_dis, idx_cluster = min_distance(cluster, x_list)
        if min_dis > t_hold and len(cluster) < maxNumClass:
            cluster.append([list(x_list[0])])
            # x_list = list(np.concatenate([x_list[0:min_dis_arg], x_list[min_dis_arg+1:]],axis=0))
            x_list = np.delete(x_list, 0, axis=0)
        else:
            cluster[idx_cluster].append(list(x_list[0]))
            # x_list = list(np.concatenate([x_list[0:min_dis_arg], x_list[min_dis_arg+1:]],axis=0))
            x_list = np.delete(x_list, 0, axis=0)
    return cluster
