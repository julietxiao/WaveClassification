'''
————欧氏距离
	f=文件实际频率时 一个样本中1个侧面数据求欧氏距离(标准正弦值－实际数据值)
'''
import matplotlib.pyplot as plt
import numpy as np
import math
import os

def fuc_sin_val(x,arg):								#标准正弦函数表达式
	w=2*(math.pi)*arg/1600
	A=511.713
	C=(math.pi)/2
	y=A*(math.sin(w*x + C))
	return y

def sin_val_onecolumn(arg):						#标准正弦函数表达式求值
	f = open('F:\\Desktop\\sin_val_onecolumn.txt','a')
	for x in range(4700):
		sin_val=fuc_sin_val(x,arg)
		f.write(str(sin_val)+'\n')
	f.close()

def sub_val_onecolumn(real_val,arg):				#实际值与标准正弦值求差值
	f = open('F:\\Desktop\\sub_val_onecolumn.txt','a')
	for x in range(4700):
		sin_val=fuc_sin_val(x,arg)
		sub_val=sin_val - real_val[x]
		sub_val=float('%.3f' % sub_val)
		f.write(str(sub_val)+'\n')
	f.close()

def distance_val_onecolumn(real_val,arg):			#实际值与标准正弦值求差值
	distance_sum = 0
	for x in range(4700):
		sin_val=fuc_sin_val(x,arg)
		dis_val=pow((sin_val - real_val[x]),2)
		distance_sum += dis_val
	distance_onecolumn = math.sqrt(distance_sum)
	return distance_onecolumn

def main():
	arr = np.loadtxt('F:\\Desktop\\20150824190534Record.txt')
	arr_6=arr[:,:-3]
	real_val=arr_6[29:4729,0]
	# np.savetxt('F:/Desktop/real_val_onecolumn.txt',real_val,fmt="%.3f")

	arr_f=arr[:,-1]
	arg=sum(arr_f)/4800		#计算文件实际频率

	# sin_val_onecolumn(arg)
	# sub_val_onecolumn(real_val,arg)

	distance_onecolumn=distance_val_onecolumn(real_val,arg)
	print(distance_onecolumn)

if __name__ == '__main__':
    main()