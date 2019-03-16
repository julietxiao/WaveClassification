# -*- coding:utf-8 -*-
import os
import pandas as pd
import numpy as np
np.set_printoptions(precision=2)

#提取出原波形数据
def extract_data(readfile):
    # 一组波形数据(4800*9)
    data = []
    # with 语句可以自动调用close方法
    with open(readfile,'r') as f:
        line = f.readline()
        while line:
            # 按行读取数据文件,每行数据以数组形式返回
            eachline = line.split()
            # 转为float型浮点数,这里我只取了电流和电压
            read_data = [float(x) for x in eachline[0:6]]
            data.append(read_data)
            line = f.readline()
    return data

# 将原始数据提取最大值然后归一化,再写入新的文件中
def normalize(data,extract_p=120):
    # 每32个点是一个周期,从中选取绝对值最大的两个值
    # 对UA,UB,UC,IA,IB,IC都这样做一遍
    period = 32
    new_data = []
    # 对齐每个视角的不同波形
    for v in range(6):
        maxIndex = 0
        maxD = data[v,0]
        for p in range(1, period):
            if maxD < data[v, p]:
                # print(data[v, p])
                maxIndex = p
                maxD = data[v, p]
        # 将该波形数据提取出120个周期的数据,同时进行归一化
        new_data.append((data[v][maxIndex:maxIndex+extract_p*period])/maxD)
    new_data = np.array(new_data)
    return new_data

# 将原本波形中的4800的特征点筛选出一部分
path = 'data'
writePath = 'processedData'
# 当前路径下所有数据文件
for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    file_path_w = os.path.join(writePath,filename)
    data = extract_data(file_path)
    print (data)
    data = np.array(data)  #data: 4800*6
    # 将数据分成6条波形数据
    data = np.transpose(data) #data: 6*4800
    data = normalize(data)
    print (data[3])
    break
