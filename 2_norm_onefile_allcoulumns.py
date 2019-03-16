'''
	一个样本中6个侧面数据归一化后的结果
'''
import os
import pandas as pd 
import numpy as np
import math

def norm_onefile(arr):
	list=[]
	i=0
	while i<6:										#取文件中的每一列数据
		arr_column=np.array(arr[:,i])
		#print(arr_column)

		start,end=0,32									#每列数据分成150个周期，每周期有32个数据
		value_list=[]
		while end<=4800:
		    #arr_cycle=arr_column[start:end])			#取每列的每周期的数据
		    value_max=max(arr_column[start:end])		#取每周期中的最大值(最高点)
		    value_min=min(arr_column[start:end])		#取每周期中的最小值(最低点)
		    value=(value_max+abs(value_min))/2			
		    value=float('%.3f' % value)
		    value_list.append(value)					#将每个周期的计算值存到列表value_list中

		    start+=32
		    end+=32    

		norm=(math.fsum(value_list))/150				#代入公式，求归一化系数norm
		norm=float('%.3f' % norm)						
		#print("第1个样本数据的第{}个侧面数据的归一化系数为:\n{}".format(i+1,norm))
		list.append(norm)
		arr_column1=arr_column/norm						#对每一列数据进行归一化处理
		arr_column1=np.around(arr_column1,decimals=3)	
		# print("第1个样本数据的第{}个侧面数据的归一化系数为:{}\n归一化结果为:\n{}".format(i+1,norm,arr_column1))
		# print()
		i+=1
	return list

def main():
	arr = np.loadtxt('G:\\Desktop\\20150824190534Record.txt')
	list = norm_onefile(arr)
	print(list)
if __name__ == '__main__':
    main()