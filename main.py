# -*- coding:utf-8 -*-
from Cluster import *
# 读入处理后的数据,这一步可以自行调整
path = 'processedData'
#此时得到的数据类型(502, 6, 3840),numpy里的array类型
# 数据格式是(样本数,视角数,各个视角维度)
data = readData(path)
#此时维度换了一下,得到(6, 502, 3840)
# 数据格式是(视角数,样本数,各个视角维度)
data = data.swapaxes(0,1)
# ---------------------------
print('数据已读取完毕,进行聚类')
num_clusters = 4  #聚类数
# 获取超级质心,以及每个视角下质心与超级质心的距离
super_center, level_view = get_super_center(data, num_clusters)
print ('每个视角的置信等级如下')
print (level_view)
print(super_center.shape) #超级质心的数据(4, 3840)即(num_cluster,dim)
# 得到样本的聚类
labels, center, loop, confi = ICMK(data, super_center, level_view, num_clusters)
print(labels)
print(loop)
