'''
————欧氏距离
	f=文件实际频率时 一个样本中6个侧面数据求norm、mark、real值、sin值、欧氏距离
'''
import os
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt

length =4700

def mark_onefile(arr_6):			#取每列数据第一个周期的正值极值点的索引
	i=0
	mark=[]
	while i<6:
		arr_column=np.array(arr_6[:,i])
		arr_column_list=list((arr_column[0:32]))
		val_max=max(arr_column_list)
		val_max_index=arr_column_list.index(val_max)
		mark.append(val_max_index)
		i+=1
	return mark

def norm_onefile(arr_6):			#取每列数据的归一化系数norm(幅值A)
	norm_list=[]
	i=0
	while i<6:
		arr_column=np.array(arr_6[:,i])
		start,end=0,32
		value_list=[]
		while end<=4800:
		    value_max=max(arr_column[start:end])
		    value_min=min(arr_column[start:end])
		    value=(value_max+abs(value_min))/2
		    #value=float('%.3f' % value)
		    value_list.append(value)
		    start+=32
		    end+=32    
		norm=(math.fsum(value_list))/150	#代入公式，求归一化系数norm
		#norm=float('%.3f' % norm)
		norm_list.append(norm)
		i+=1
	return norm_list

def fuc_sin_val(x,norm_column,arg):		#标准正弦函数表达式
	w=2*(math.pi)*arg/1600
	A=norm_column
	C=(math.pi)/2
	y =A*(math.sin(w*x + C))
	return y

def fuc_sin_val_column(norm_column,arg):				#标准正弦函数表达式求值
	sin_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,norm_column,arg)
		sin_val_column.append(sin_val)
	return sin_val_column

def fuc_sub_val_column(real_val_column,norm_column,arg):			#实际值与标准正弦值求差值
	sub_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,norm_column,arg)
		sub_val=sin_val - real_val_column[x]
		#sub_val=float('%.3f' % sub_val)
		sub_val_column.append(sub_val)
	return sub_val_column

def distance_val_onecolumn(real_val_column,norm_column,arg):		#实际值与标准正弦值求欧氏距离
	distance_sum = 0
	for x in range(length):
		sin_val=fuc_sin_val(x,norm_column,arg)
		dis_val=pow((sin_val - real_val_column[x]),2)
		distance_sum += dis_val
	distance_onecolumn = math.sqrt(distance_sum)
	return distance_onecolumn

def deal_onefile(arr):		#处理一个文件
	arr_6=arr[:,:-3]		#提取本文件前6列数据
	arr_f=arr[:,-1]
	arg=sum(arr_f)/4800		#计算本文件实际频率

	norm_list = norm_onefile(arr_6)		#每列数据的归一化系数(幅值A)数组norm_list
	mark = mark_onefile(arr_6)			#每列数据第一个周期的正值极值点索引数组mark

	norm_column=norm_list[0]	#第i列数据的幅值A
	mark_column=mark[0]			#第i列数据第一个周期的正值极值点索引
	real_val_columns=arr_6[mark_column:mark_column+length,0]#第i列数据选取起终区间
	sin_val_columns=fuc_sin_val_column(norm_column,arg)
	sub_val_columns=fuc_sub_val_column(real_val_columns,norm_column,arg)
	
	distance_list=[]
	distance_onecolumn=distance_val_onecolumn(real_val_columns,norm_column,arg)
	distance_list.append(distance_onecolumn)

	for i in range(5):
		norm_column=norm_list[i+1]	#第i列数据的幅值A
		mark_column=mark[i+1]			#第i列数据第一个周期的正值极值点索引
		real_val_column=arr_6[mark_column:mark_column+length,i+1]#第i列数据选取起终区间
		# sin_val_column=fuc_sin_val_column(norm_column,arg)
		# sub_val_column=fuc_sub_val_column(real_val_column,norm_column,arg)

		# real_val_columns=np.column_stack((real_val_columns,real_val_column))
		# sin_val_columns=np.column_stack((sin_val_columns,sin_val_column))
		# sub_val_columns=np.column_stack((sub_val_columns,sub_val_column))
		
		distance_onecolumn=distance_val_onecolumn(real_val_column,norm_column,arg)
		distance_list.append(distance_onecolumn)
	return distance_list
	# np.savetxt('F:\\Desktop\\real_val_columns.txt',real_val_columns,fmt="%.3f")
	# np.savetxt('F:\\Desktop\\sin_val_columns.txt',sin_val_columns,fmt="%.3f")
	# np.savetxt('F:\\Desktop\\sub_val_columns.txt',sub_val_columns,fmt="%.3f")
	# gather_list = np.column_stack((sin_val_onecolumn, real_val_onecolumn, sub_val_onecolumn))

def main():
	arr = np.loadtxt('F:\\Desktop\\20150824190534Record.txt')
	distance_list=deal_onefile(arr)
	print(distance_list)

if __name__ == '__main__':
    main()




