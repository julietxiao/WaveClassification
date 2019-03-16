'''
	一个侧面数据在502个样本中归一化后的结果
'''

import os
import pandas as pd 
import numpy as np
import math

res=r'G:\\Desktop\\风机\\code\\2_datasorting\\'          		#处理前原始所有dat文件所在的文件夹
list = r'G:\\Desktop\\风机\\code\\1_datalist.txt' 		 #dat数据名字汇总txt
savePath=r'G:\\Desktop\\2_norm_allfiles_onecolumn\\'  		 #处理后保存所有dat文件所在的文件夹

f = open(list,'r')							#从汇总txt逐个读取原始文件
lines = f.readlines()
j=0
for line in lines[:]:
	name = line.strip()
	resfile=res+name[:-4]+'.txt' 
	savefile=savePath+name[:-4]+'.txt'			#每次处理后的txt文件保存路径

	arr = np.loadtxt(resfile)
	arr_column=np.array(arr[:,0])					#取文件中的每一列数据
	#print(arr_column)

	start,end=0,32									#每列数据分成150个周期，每周期有32个数据
	i=0
	value_list=[]
	while end<=64:
	    #arr_cycle=np.array(arr_column[start:end])	#取每列的每周期的数据
		value_max=max(arr_column[start:end])		#取每周期中的最大值(最高点)
		value_min=min(arr_column[start:end])		#取每周期中的最小值(最低点)
		value=(value_max+abs(value_min))/2			
		value=float('%.3f' % value)
		value_list.append(value)					#将每个周期的计算值存到列表value_list中

		start+=32
		end+=32    
		i+=1

	norm=(math.fsum(value_list))/2				#代入公式，求归一化系数norm
	norm=float('%.3f' % norm)						
	#print(norm) 150

	arr_column1=arr_column/norm						#对每一列数据进行归一化处理
	arr_column1=np.around(arr_column1,decimals=3)	
	#print(arr_column1)
	#print(len(arr_column1)) 1800
	#print("第1个侧面数据的第{}个样本数据的归一化结果为:\n{}".format(j+1,arr_column1))
	j+=1
	
	np.savetxt(savefile,arr_column1,fmt="%.3f")

#writeFileHandle.close()