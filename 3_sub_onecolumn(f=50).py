'''
	f=50时一个样本中1个侧面数据求norm、mark、real值、sin值、差值、绘图
'''
import os
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt

length =4700

def mark_onefile(arr):									#取每列数据第一个周期的正值极值点的索引
	i=0
	mark=[]
	while i<6:
		arr_column=np.array(arr[:,i])
		arr_column_list=list((arr_column[0:32]))
		val_max=max(arr_column_list)
		val_max_index=arr_column_list.index(val_max)
		mark.append(val_max_index)
		i+=1
	return mark

def norm_onefile(arr):									#取每列数据的归一化系数norm(幅值A)
	norm_list=[]
	i=0
	while i<6:
		arr_column=np.array(arr[:,i])
		start,end=0,32
		value_list=[]
		while end<=4800:
		    value_max=max(arr_column[start:end])
		    value_min=min(arr_column[start:end])
		    value=(value_max+abs(value_min))/2
		    value=float('%.3f' % value)
		    value_list.append(value)
		    start+=32
		    end+=32    

		norm=(math.fsum(value_list))/150				#代入公式，求归一化系数norm
		norm=float('%.3f' % norm)
		norm_list.append(norm)
		i+=1
	return norm_list

def fuc_sin_val(x,norm_column):							#标准正弦函数表达式
	w=2*(math.pi)/32
	A=norm_column
	C=(math.pi)/2
	y=A*(math.sin(w*x + C))
	return y
def sin_val_onecolumn(norm_column):						#标准正弦函数表达式求值
	sub_val_list=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,norm_column)
		sub_val_list.append(sin_val)
	return sub_val_list
def sub_val_onecolumn(real_val,norm_column):			#实际值与标准正弦值求差值
	sub_val_list=[]
	for x in range(4700):
		sin_val=fuc_sin_val(x,norm_column)
		sub_val=sin_val - real_val[x]
		sub_val=float('%.3f' % sub_val)
		sub_val_list.append(sub_val)
	return sub_val_list

def main():
	arr = np.loadtxt('G:\\Desktop\\20150915222435Record.txt')
	norm_list = norm_onefile(arr)					#每列数据的归一化系数(幅值A)数组norm_list
	mark = mark_onefile(arr)						#每列数据第一个周期的正值极值点索引数组mark

	#for i in range(6):
	norm_column=norm_list[2]
	mark_column=mark[2]
	real_val=arr[mark_column:mark_column+length,2]
	sin_val_list=sin_val_onecolumn(norm_column)
	sub_val_list=sub_val_onecolumn(real_val,norm_column)

	gather_list = np.column_stack((sin_val_list, real_val, sub_val_list))
	np.savetxt('G:\\Desktop\\1_val_onecolumn.txt',gather_list,fmt="%.3f")
	arr = np.loadtxt('G:\\Desktop\\1_val_onecolumn.txt')

	x=list(range(length))					#绘制一个样本中1个侧面数据标准正弦图、实际数据点和差值图
	sin_arr=list(gather_list[0:length,0])
	real_arr=list(gather_list[0:length,1])
	sub_arr=list(gather_list[0:length,2])
	plt.plot(x,sin_arr,'g',x,real_arr,'r',x,sub_arr,'b')
	plt.show()


if __name__ == '__main__':
    main()