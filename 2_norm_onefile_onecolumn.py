'''
	一个样本中1个侧面数据归一化后的结果
'''
import os
import pandas as pd
import numpy as np
import math

resfile = 'G:\\Desktop\\20150824190534Record.txt'
arr = np.loadtxt(resfile)
arr_column=np.array(arr[:,0])					#取文件中的每一列数据

start,end=0,32									#每列数据分成150个周期，每周期有32个数据
i=0
value_list=[]
while end<=4800:
    #arr_cycle=np.array(arr_column[start:end])	#取每列的每周期的数据
    value_max=max(arr_column[start:end])		#取每周期中的最大值(最高点)
    value_min=min(arr_column[start:end])		#取每周期中的最小值(最低点)
    value=(value_max+abs(value_min))/2			
    value=float('%.3f' % value)
    value_list.append(value)					#将每个周期的计算值存到列表value_list中

    start+=32
    end+=32    
    i+=1

print(len(value_list))
norm=(math.fsum(value_list))/150				#代入公式，求归一化系数norm
norm=float('%.3f' % norm)						
print(norm)

arr_column1=arr_column/norm						#对每一列数据进行归一化处理
arr_column1=np.around(arr_column1,decimals=3)	
print(arr_column1)

 