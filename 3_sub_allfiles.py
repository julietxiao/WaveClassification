'''
	f=文件实际频率时 所有样本中6个侧面数据求norm、mark、real值、sin值、差值、绘图
'''
import os
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt

length =4700
def mark_onefile(arr_6):		#取每列数据第一个周期的正值极值点的索引
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

def norm_onefile(arr_6):		#取每列数据的归一化系数norm(幅值A)
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
		    value_list.append(value)
		    start+=32
		    end+=32    
		norm=(math.fsum(value_list))/150	#代入公式，求归一化系数norm
		#norm=float('%.3f' % norm)
		norm_list.append(norm)
		i+=1
	return norm_list

def fuc_sin_val(x,norm_column,arg):			#标准正弦函数表达式
	w=2*(math.pi)*arg/1600
	A=norm_column
	C=(math.pi)/2
	y =A*(math.sin(w*x + C))
	return y
def fuc_sin_val_column(norm_column,arg):	#标准正弦函数表达式求值
	sin_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,norm_column,arg)
		sin_val_column.append(sin_val)
	return sin_val_column
def fuc_sub_val_column(real_val_column,norm_column,arg):	#实际值与标准正弦值求差值
	sub_val_column=[]
	for x in range(4700):
		sin_val=fuc_sin_val(x,norm_column,arg)
		sub_val=sin_val - real_val_column[x]
		#sub_val=float('%.3f' % sub_val)
		sub_val_column.append(sub_val)
	return sub_val_column

def draw_chart():	#绘制1个样本中1个侧面数据标准正弦图、实际数据点和差值图
	x=list(range(length))
	sin_arr=list(gather_list[0:length,0])
	real_arr=list(gather_list[0:length,1])
	sub_arr=list(gather_list[0:length,2])
	plt.plot(x,sin_arr,'g',x,real_arr,'r',x,sub_arr,'b')
	plt.show()

def deal_onefile(arr):#1个样本中6个侧面数据求norm、mark、real值、sin值、差值
	arr_6=arr[:,:-3]		#提取本文件前6列数据
	arr_f=arr[:,-1]
	arg=sum(arr_f)/4800		#计算本文件实际频率

	norm_list = norm_onefile(arr_6)	#每列数据的归一化系数(幅值A)数组norm_list
	mark = mark_onefile(arr_6)		#每列数据第一个周期的正值极值点索引数组mark
	#第1个侧面数据
	norm_column=norm_list[0]	#第i列数据的幅值A
	mark_column=mark[0]			#第i列数据第一个周期的正值极值点索引
	real_val_columns=arr_6[mark_column:mark_column+length,0]#第i列数据选取起终区间
	sin_val_columns=fuc_sin_val_column(norm_column,arg)
	sub_val_columns=fuc_sub_val_column(real_val_columns,norm_column,arg)
	#后5个侧面数据
	for i in range(5):
		norm_column=norm_list[i+1]	#第i列数据的幅值A
		mark_column=mark[i+1]		#第i列数据第一个周期的正值极值点索引
		real_val_column=arr_6[mark_column:mark_column+length,i+1]#第i列数据选取起终区间
		sin_val_column=fuc_sin_val_column(norm_column,arg)
		sub_val_column=fuc_sub_val_column(real_val_column,norm_column,arg)
		#column_stack将每列数据整合到一个数组中
		real_val_columns=np.column_stack((real_val_columns,real_val_column))
		sin_val_columns=np.column_stack((sin_val_columns,sin_val_column))
		sub_val_columns=np.column_stack((sub_val_columns,sub_val_column))
	return real_val_columns,sin_val_columns,sub_val_columns
	
def main():
	res=r'G:\\Desktop\\1_datasorting_allfiles(9)\\' #处理前原始所有文件所在的文件夹
	list = r'G:\\Desktop\\1_datalist.txt' #res数据名字汇总txt
	real_val_Path=r'G:\\Desktop\\3_real_val_files\\' #处理后所有real_val所在的文件夹
	sin_val_Path=r'G:\\Desktop\\3_sin_val_files\\' #处理后所有sin_val所在的文件夹
	sub_val_Path=r'G:\\Desktop\\3_sub_val_files\\' #处理后所有sub_val所在的文件夹

	f = open(list,'r')		#从汇总txt逐个读取原始文件
	lines = f.readlines()
	for line in lines[:]:
		name = line.strip()
		resfile=res+name[:-4]+'.txt'	#每次要处理的文件路径
		arr = np.loadtxt(resfile)
		real_val_columns,sin_val_columns,sub_val_columns=deal_onefile(arr)
		#每次处理后文件的保存路径 _val_Path
		real_val_file=real_val_Path+name[:-4]+'.txt'
		sin_val_file=sin_val_Path+name[:-4]+'.txt'
		sub_val_file=sub_val_Path+name[:-4]+'.txt'
		#将处理后的数组 _val_columns放入 _val_file文件保存路径中
		np.savetxt(real_val_file,real_val_columns,fmt="%.3f")
		np.savetxt(sin_val_file,sin_val_columns,fmt="%.3f")
		np.savetxt(sub_val_file,sub_val_columns,fmt="%.3f")

if __name__ == '__main__':
    main()