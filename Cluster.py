# -*- coding: utf-8 -*-
import os
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

View = 6
# 读入处理后的数据,将文件夹中的数据返回到三维数组中
def readData(path):
    data = []
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        a = np.loadtxt(file_path)
        data.append(a)

    data = np.array(data)
    return data


# 用基本kmeans方法来获取超级质心
# 基本思路是,按照顺序将各个视角下的质心依次传递,
# 最后平均各个视角的质心得到超级质心
def get_super_center(data, num_clusters):
    label_pred = [] #每个视角下的聚类标签
    centers = [] #每个视角下的聚类质心
    dim = data.shape[2]
    # 构造聚类器
    km = KMeans(
        n_clusters = num_clusters
    )
    # 从UA角度开始训练
    km.fit(data[0])
    # 获取UA聚类标签,聚类中心
    # label_pred.append(km.labels_)
    centers.append(km.cluster_centers_)
    center_temp = km.cluster_centers_
    for v in range(1,View):
        # 构造初始化质心的kmeans聚类器
        km_for_v = KMeans(n_clusters=num_clusters, init=center_temp, n_init=1)
        km_for_v.fit(data[v])
        # label_pred.append(km_for_v.labels_)
        centers.append(km_for_v.cluster_centers_)
        center_temp = km_for_v.cluster_centers_

    #得到各个视角的聚类质心后,求平均值,得超级质心
    centers = np.array(centers)
    super_center = np.mean(centers, axis=0)
    # 顺便算下每个视角下的质心与超级质心的距离
    # aver_distance = []
    level_view = []
    for v in range(6):
        # 默认是求矩阵的F范数
        dist = np.linalg.norm(centers[v]-super_center)
        # aver_distance.append(dist/dim)
        level_view.append(dim/dist)

    return super_center, level_view



# 开始进入聚类
def ICMK(data, super_center, level, num_clusters):
    n_instances = data.shape[1]
    max_iter = 100
    labels = np.zeros(n_instances)
    labels_new = np.zeros(n_instances)
    label_change = True
    loop = 1
    center_v = super_center
    # 初始化置信矩阵C
    confi = np.zeros([n_instances, num_clusters])
    while label_change and loop <= max_iter:
        loop += 1
        for v in range(View):
            # 从UA视角开始初始化
            km = KMeans(
                n_clusters=num_clusters,
                init=center_v,
                n_init=1
            )
            # 从UA角度开始训练
            km.fit(data[v])
            # 省略指示矩阵G.用数组形式代替
            label_v = km.labels_
            # print (label_v)
            # 聚类中心矩阵F
            center_v = km.cluster_centers_
            # 本轮kmeans的循环次数
            loop_v = km.n_iter_
            print ('在'+str(v)+'视角下kmeans循环次数:'+str(loop_v))

            # 记录样本的置信矩阵
            for k in range(num_clusters):
                # 样例中被分到k类的样本索引
                k_ins = np.nonzero(label_v == k)[0]
                # 置信矩阵中加入相应的等级
                confi[k_ins, k] += level[v]

            labels_new = label_v

        label_change = not ((labels == labels_new).all())
        labels = labels_new

    # 根据置信矩阵来选取每个置信度最高的label(每行最大值)
    for i in range(n_instances):
        ins_k = np.argmax(confi[i])
        labels[i] = ins_k
    return labels, center_v, loop, confi




