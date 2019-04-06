'''
	f=文件实际频率时一个样本中6个侧面数据
	求每个数据点对应到f=50下,real_val导数方向移动△x后的对应值
'''
import os
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt

length =4700

# 取每列数据第一个周期的正值极值点的索引
def mark_onefile(arr_6):
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

# 取每列数据的归一化系数norm(幅值A)
def norm_onefile(arr_6):
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

# 标准正弦函数表达式(f=文件实际频率时)
def fuc_sin_val(x,norm_column,arg):
	w=2*(math.pi)*arg/1600
	A=norm_column
	C=(math.pi)/2
	y =A*(math.sin(w*x + C))
	return y
# 标准正弦函数表达式求值(f=文件实际频率时)
def fuc_sin_val_column(norm_column,arg):
	sin_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,norm_column,arg)
		sin_val_column.append(sin_val)
	return sin_val_column
# 实际值与标准正弦值求差值(f=文件实际频率时)
def fuc_sub_val_column(real_val_column,norm_column,arg):
	sub_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,norm_column,arg)
		sub_val=sin_val - real_val_column[x]
		#sub_val=float('%.3f' % sub_val)
		sub_val_column.append(sub_val)
	return sub_val_column

# 标准反正弦函数表达式(f=50)
def fuc_sin_x(y,norm_column,arg):
	w=2*(math.pi)/32
	A=norm_column
	C=(math.pi)/2
	x=(math.asin(y/A)-C)/w
	return x
# 标准正弦函数表达式求不同f下相同y值对应的x值(f=50)
def fuc_sin_x_column(norm_column,arg):
	sin_x_column=[]
	sin_val1_column=[]
	for x in range(length):
		y=fuc_sin_val(x,norm_column,arg)
		cycle_n=(x//32)*32	#是第几个周期的x
		sin_x=fuc_sin_x(y,norm_column,arg)+cycle_n
		sin_x_column.append(sin_x)
	return sin_x_column
# 实际值与(x+△x)下对应的标准正弦值求差值(f=文件实际频率时)
def fuc_sub_y_column(real_val_column,norm_column,arg):
	sub_y_column=[]
	sin_x_column=fuc_sin_x_column(norm_column,arg)
	for x in range(length):
		sub_y=sin_y_column[x] - real_val_column[x]
		sub_y_column.append(sub_y)
	return sub_y_column

# 标准正弦函数导数表达式(f=文件实际频率时)
def fuc_derivative(x,norm_column,arg):
	w=2*(math.pi)*arg/1600
	A=norm_column
	C=(math.pi)/2
	y=A*w*(math.cos(w*x + C))
	return y
# 标准正弦函数表达式求移动后下实际值对应的值(f=文件实际频率时)
def fuc_trans_val_column(arg,norm_column,real_val_column):
	trans_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,norm_column,arg)
		cycle_n=(x//32)*32	#是第几个周期的x
		sin_x=fuc_sin_x(sin_val,norm_column,arg)+cycle_n
		sin_x=x-sin_x	#求△x的值

		derivative_y=fuc_derivative(x,norm_column,arg)	#x点处的导数值(f=文件实际频率时)
		trans_val=real_val_column[x]+derivative_y*sin_x*arg/1600
		trans_val_column.append(trans_val)
	return trans_val_column
# 实际值与标准正弦值求差值
def fuc_sub_trans_column(real_val_column,norm_column,arg):
	sub_trans_column=[]
	trans_val_column=fuc_trans_val_column(arg,norm_column,real_val_column)
	sin_x_column=fuc_sin_x_column(norm_column,arg)
	for x in range(length):
		trans_sub=trans_val_column[x]-real_val_column[x]
		sub_trans_column.append(trans_sub)
	return sub_trans_column

#绘制一个样本中1个侧面数据标准正弦图、实际数据点和差值图
def draw_chart():
	x=list(range(length))
	sin_arr=list(gather_list[0:length,0])
	real_arr=list(gather_list[0:length,1])
	sub_arr=list(gather_list[0:length,2])
	plt.plot(x,sin_arr,'g',x,real_arr,'r',x,sub_arr,'b')
	plt.show()

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
	sin_x_columns=fuc_sin_x_column(norm_column,arg)
	#sub_y_columns=fuc_sub_y_column(real_val_columns,norm_column,arg)
	trans_val_columns=fuc_trans_val_column(arg,norm_column,real_val_columns)
	sub_trans_columns=fuc_sub_trans_column(real_val_columns,norm_column,arg)

	for i in range(5):
		norm_column=norm_list[i+1]	#第i列数据的幅值A
		mark_column=mark[i+1]			#第i列数据第一个周期的正值极值点索引
		real_val_column=arr_6[mark_column:mark_column+length,i+1]#第i列数据选取起终区间
		sin_val_column=fuc_sin_val_column(norm_column,arg)
		sub_val_column=fuc_sub_val_column(real_val_column,norm_column,arg)
		sin_x_column=fuc_sin_x_column(norm_column,arg)
		#sub_y_column=fuc_sub_y_column(real_val_columns,norm_column,arg)
		trans_val_column=fuc_trans_val_column(arg,norm_column,real_val_column)
		sub_trans_column=fuc_sub_trans_column(real_val_column,norm_column,arg)

		real_val_columns=np.column_stack((real_val_columns,real_val_column))
		sin_val_columns=np.column_stack((sin_val_columns,sin_val_column))
		sub_val_columns=np.column_stack((sub_val_columns,sub_val_column))
		sin_x_columns=np.column_stack((sin_x_columns,sin_x_column))
		trans_val_columns=np.column_stack((trans_val_columns,trans_val_column))
		sub_trans_columns=np.column_stack((sub_trans_columns,sub_trans_column))

	np.savetxt('G:\\Desktop\\real_val_columns.txt',real_val_columns,fmt="%.3f")
	np.savetxt('G:\\Desktop\\sin_val_columns.txt',sin_val_columns,fmt="%.3f")
	np.savetxt('G:\\Desktop\\sub_val_columns.txt',sub_val_columns,fmt="%.3f")
	np.savetxt('G:\\Desktop\\sin_x_columns.txt',sin_x_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\sub_y_columns.txt',sub_y_columns,fmt="%.3f")
	np.savetxt('G:\\Desktop\\trans_val_columns.txt',trans_val_columns,fmt="%.3f")
	np.savetxt('G:\\Desktop\\sub_trans_column.txt',sub_trans_columns,fmt="%.3f")

	# gather_list = np.column_stack((sin_val_onecolumn, real_val_onecolumn, sub_val_onecolumn))

def main():
	arr = np.loadtxt('G:\\Desktop\\1_datasorting_allfiles(9)\\20150824190534Record.txt')
	deal_onefile(arr)

if __name__ == '__main__':
    main()
