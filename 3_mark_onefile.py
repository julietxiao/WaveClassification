'''
	数据清洗：一个样本中6个侧面数据 每隔10个周期 相位对齐一次
'''
import os
import pandas as pd 
import numpy as np
import math

def mark_onefile(arr):									#取第一个周期的正值极值点的索引
	i=0
	#mark=[]
	while i<6:											#取文件中的每一列数据
		arr_column=np.array(arr[:,i])
		start,end=0,32
		mark_10cycle=[]
		j=0
		while end<=4800:
			arr_column_list=list((arr_column[start:end]))
			val_max=max(arr_column_list)					#取第一个周期的正值极值点
			val_max_index=(arr_column_list).index(val_max)				#取第一个周期的正值极值点的索引
			mark_10cycle.append(val_max_index+j*320)
			start+=320
			end+=320
			j+=1
		print(mark_10cycle)
		i+=1
	#return mark

def main():
	arr = np.loadtxt('G:\\Desktop\\20150824190534Record.txt')
	mark_onefile(arr)
	#print(mark)

if __name__ == '__main__':
    main()
