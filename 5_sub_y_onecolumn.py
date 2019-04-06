'''
	f=文件实际频率时一个样本中1个侧面数据
	求每个数据点对应到f=50下,x值带入f=文件实际频率时正弦函数的对应值
'''
import os
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt

length =4700

def fuc_sin_val(x,arg):		#标准正弦函数表达式求y(f=文件实际频率时)
	w=2*(math.pi)*arg/1600
	A=512.128
	C=(math.pi)/2
	y =A*(math.sin(w*x + C))
	return y

def fuc_sin_val_column(arg):		#标准正弦函数表达式求值(f=文件实际频率时)
	sin_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,arg)
		sin_val_column.append(sin_val)
	return sin_val_column

def fuc_sub_val_column(real_val_columns,arg):			#实际值与标准正弦值求差值
	sub_val_column=[]
	for x in range(length):
		sin_val=fuc_sin_val(x,arg)
		sub_val=sin_val - real_val_columns[x]
		sub_val_column.append(sub_val)
	return sub_val_column

def fuc_sin_x(y,arg):		#标准正弦函数表达式求x(f=50)
	w=2*(math.pi)/32
	A=512.128
	C=(math.pi)/2
	x=(math.asin(y/A)-C)/w
	return x

def fuc_sin_x_column(arg):				#标准正弦函数表达式求值(f=50)
	sin_x_column=[]
	sin_y_column=[]
	for x in range(length):
		y=fuc_sin_val(x,arg)
		cycle_n=(x//32)*32	#是第几个周期的x
		sin_x=fuc_sin_x(y,arg)+cycle_n
		sin_x_column.append(sin_x)

		sin_y=fuc_sin_val(sin_x,arg)
		sin_y_column.append(sin_y)
	return sin_x_column,sin_y_column

def fuc_sub_y_column(real_val_columns,arg):			#实际值与标准正弦值求差值
	sub_y_column=[]
	sin_x_column,sin_y_column=fuc_sin_x_column(arg)
	for x in range(length):
		sub_y=sin_y_column[x] - real_val_columns[x]
		sub_y_column.append(sub_y)
	return sub_y_column

def deal_onefile(arr):		#处理一个文件
	arr_6=arr[:,:-3]		#提取本文件前6列数据
	arr_f=arr[:,-1]
	arg=sum(arr_f)/4800		#计算本文件实际频率

	real_val_columns=arr_6[29:29+length,0]#第i列数据选取起终区间
	sin_val_columns=fuc_sin_val_column(arg)
	sin_x_columns,sin_y_columns=fuc_sin_x_column(arg)
	sub_y_columns=fuc_sub_y_column(real_val_columns,arg)
	# sub_val_columns=fuc_sub_val_column(real_val_columns,arg)
	# np.savetxt('G:\\Desktop\\sub_val_columns.txt',sub_val_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\real_val_columns.txt',real_val_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\sin_val_columns.txt',sin_val_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\sin_x_columns.txt',sin_x_columns,fmt="%.3f")
	# np.savetxt('G:\\Desktop\\sin_y_columns.txt',sin_y_columns,fmt="%.3f")
	np.savetxt('G:\\Desktop\\sub_y_columns.txt',sub_y_columns,fmt="%.3f")
def main():
	arr = np.loadtxt('G:\\Desktop\\20150824190534Record.txt')
	deal_onefile(arr)

if __name__ == '__main__':
    main()