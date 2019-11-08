# -*- coding:utf-8 -*-
# 这个程序写的有问题
import numpy as np

def distEclud(vecA, vecB):
    return np.linalg.norm(vecA - vecB)

# 比sklearn中kmeans多了个记录每个样本的转移次数
def km_icmk(data, centers, tol = 0.0001):
    n_instances = data.shape[0]
    n_clusters = centers.shape[0]
    shift = np.zeros([n_instances], int)
    label = np.zeros([n_instances], int)
    label.fill(-1)
    # 指示矩阵,为后续算质心做好准备
    # G = np.mat(np.zeros([n_instances,n_clusters]))
    cluster_changed = True
    loop = 0
    while cluster_changed:
        loop += 1
        # 开始进行聚类
        for i in range(n_instances):
            minDist = np.inf
            minIndex = -1
            for k in range(n_clusters):
                # 计算该样本与k类质心的距离
                dist_ik = distEclud(data[i], centers[k])
                if dist_ik<minDist:
                    minDist = dist_ik
                    minIndex = k
            if label[i] == -1:
                label[i] = minIndex
                # G[i][minIndex] = 1
            elif label[i] != minIndex:
                shift[i] += 1
                label[i] = minIndex
                # G[i][minIndex] = 1
        new_center = []
        # 重新计算此时的质心
        for k in range(n_clusters):
            cen_ins = np.nonzero(label == k)[0]
            pcluster = data[cen_ins]
            new_center.append(np.mean(pcluster, axis=0))
        # 计算新质心和之前质心的差值(收敛阈值tol可设定)
        new_centers = np.array(new_center)
        center_shift_tol = np.linalg.norm(centers-new_centers)
        if center_shift_tol > tol:
            cluster_changed = True
            centers = new_centers
        else:
            cluster_changed = False
    return label, centers, loop, shift
