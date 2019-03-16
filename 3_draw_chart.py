'''
	绘制一个样本中1个侧面数据标准正弦图、实际数据点和差值图
'''
import matplotlib.pyplot as plt
import numpy as np
import time
import math
import os

# k=4700
# arr = np.loadtxt('G:\\Desktop\\1_val_onecolumn.txt')
# x=list(range(4700))
# sin_arr=list(arr[:k,0])
# real_arr=list(arr[:k,1])
# sub_arr=list(arr[:k,2])

# # sin_arr=list(arr[k:,0])
# # real_arr=list(arr[k:,1])
# # sub_arr=list(arr[k:,2])
# plt.plot(x,sin_arr,'g',x,real_arr,'r',x,sub_arr,'b')
# plt.show()

k=470
n=3
real_val_columns = np.loadtxt('G:\\Desktop\\real_val_columns.txt')
sin_val_columns = np.loadtxt('G:\\Desktop\\sin_val_columns.txt')
sub_val_columns = np.loadtxt('G:\\Desktop\\sub_val_columns.txt')
x=list(range(k))
# real_arr=list(real_val_columns[:k,n])
# sin_arr=list(sin_val_columns[:k,n])
# sub_arr=list(sub_val_columns[:k,n])

real_arr=list(real_val_columns[-k:,n])
sin_arr=list(sin_val_columns[-k:,n])
sub_arr=list(sub_val_columns[-k:,n])
plt.plot(x,sin_arr,'g',x,real_arr,'r',x,sub_arr,'b')
plt.show()

