# -*- coding: utf-8 -*-
import os
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

# 读入处理后的数据,将文件夹中的数据返回到三维数组中
def readData(path):
    data = []
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        a = np.loadtxt(file_path)
        data.append(a)

    data = np.array(data)
    return data

# 最基本的kmeans,从视角v下的特征进行聚类
def km1(data):
    # 构造聚类器
    km = KMeans(
        n_clusters=4
    )
    km.fit(data)
    # 获取聚类标签
    label_pred = km.labels_
    print (label_pred)
    return 0
# 读入处理后的数据
path = 'processedData'
data = readData(path) #此时得到的数据类型(502, 6, 3840)
data = data.swapaxes(0,1) #此时得到(6, 502, 3840)
print('数据已读取完毕,进行聚类')
# 对视角UA下聚类
km1(data[0])



