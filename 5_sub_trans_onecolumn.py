'''
	f=文件实际频率时一个样本中1个侧面数据
	求每个数据点对应到f=50下,real_val导数方向移动△x后的对应值
'''
import os
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt

length =4700
# 标准正弦函数表达式(f=文件实际频率时)
def fuc_sin_val(x,arg):
	w=2*(math.pi)*arg/1600
	A=512.128
	C=(math.pi)/2
	y =A*(math.sin(w*x + C))
	return y
# 标准正弦函数表达式求值(f=文件实际频率时)
def fuc_sin_val_column(arg):
	sin_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,arg)
		sin_val_column.append(sin_val)
	return sin_val_column
# 实际值与标准正弦值求差值(f=文件实际频率时)
def fuc_sub_val_column(real_val_columns,arg):
	sub_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,arg)
		sub_val=sin_val - real_val_columns[x]
		sub_val_column.append(sub_val)
	return sub_val_column

# 标准反正弦函数表达式(f=50)
def fuc_sin_x(y,arg):
	w=2*(math.pi)/32
	A=512.128
	C=(math.pi)/2
	x=(math.asin(y/A)-C)/w
	return x
# 标准正弦函数表达式求不同f下相同y值对应的x值(f=50)
def fuc_sin_x_column(arg):
	sin_x_column=[]
	sin_val1_column=[]
	for x in range(length):
		y=fuc_sin_val(x,arg)
		cycle_n=(x//32)*32	#是第几个周期的x
		sin_x=fuc_sin_x(y,arg)+cycle_n
		sin_x_column.append(sin_x)
	return sin_x_column

# 标准正弦函数导数表达式(f=文件实际频率时)
def fuc_derivative(x,arg):
	w=2*(math.pi)*arg/1600
	A=512.128
	C=(math.pi)/2
	y=A*w*(math.cos(w*x + C))
	return y
# 标准正弦函数表达式求移动后下实际值对应的值(f=文件实际频率时)
def fuc_trans_val_column(arg,real_val_columns):
	trans_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,arg)
		cycle_n=(x//32)*32	#是第几个周期的x
		sin_x=fuc_sin_x(sin_val,arg)+cycle_n
		sin_x=x-sin_x

		derivative_y=fuc_derivative(x,arg)	#x点处的导数值(f=文件实际频率时)
		trans_val=real_val_columns[x]+derivative_y*sin_x*arg/1600
		trans_val_column.append(trans_val)
	return trans_val_column
# 实际值与标准正弦值求差值
def fuc_sub_trans_column(real_val_columns,arg):
	trans_sub_column=[]
	trans_val_column=fuc_trans_val_column(arg,real_val_columns)
	sin_x_column=fuc_sin_x_column(arg)
	for x in range(length):
		trans_sub=trans_val_column[x]-real_val_columns[x]
		trans_sub_column.append(trans_sub)
	return trans_sub_column

def deal_onefile(arr):		#处理一个文件
	arr_6=arr[:,:-3]		#提取本文件前6列数据
	arr_f=arr[:,-1]
	arg=sum(arr_f)/4800		#计算本文件实际频率

	real_val_columns=arr_6[29:29+length,0]#第i列数据选取起终区间
	sin_val_columns=fuc_sin_val_column(arg)
	sin_x_columns=fuc_sin_x_column(arg)
	trans_val_columns=fuc_trans_val_column(arg,real_val_columns)
	trans_sub_column=fuc_sub_trans_column(real_val_columns,arg)
	sub_val_columns=fuc_sub_val_column(real_val_columns,arg)
	np.savetxt('G:\\Desktop\\sub_val_columns.txt',sub_val_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\real_val_columns.txt',real_val_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\sin_val_columns.txt',sin_val_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\sin_x_columns.txt',sin_x_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\trans_val_columns.txt',trans_val_columns,fmt="%.3f")
	np.savetxt('G:\\Desktop\\trans_sub_column.txt',trans_sub_column,fmt="%.3f")
def main():
	arr = np.loadtxt('G:\\Desktop\\20150824190534Record.txt')
	deal_onefile(arr)

if __name__ == '__main__':
    main()