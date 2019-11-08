# -*- coding:utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt


#标准正弦函数表达式
def fuc_sin_val(x,norm_column,argf = 50):
	# argf = 50 #频率f=50, 周期T=32
	w=2*(math.pi)*argf/1600
	A=norm_column
	C=(math.pi)/2
	y =A*(math.sin(w*x + C))
	return y

# 标准正弦函数导数表达式(f=50)
def fuc_derivative(x,norm_column,argf = 50):
	w=2*(math.pi)*argf/1600
	A=norm_column
	C=(math.pi)/2
	y=A*w*(math.cos(w*x + C))
	return y

# Ax + By +C = 0 一次线性函数求交点
def get_cross_point(a1,b1,c1,a2,b2,c2):
    if a1 !=0 :
        y0 = (a2*c1-a1*c2)/(a1*b2-a2*b1)
        x0 = (c1+b1*y0)/(-a1)
        return x0, y0
    else:
        print ('导数求错了')
    return 0, 0

def point_dis(x1,y1,x2,y2):
    a1 = math.pow((x2-x1),2)
    a2 = math.pow((y2-y1),2)
    dis = math.sqrt(a1+a2)
    return dis

# delta_x 只能为整数
def new_dis(real_arr, delta_x = 1):
    dis_arr = []
    norm = real_arr[0]
    length = len(real_arr)

    for i in range(length):
        if (i%16)!=0 :
            px = i
            py = fuc_sin_val(i,norm)
        #     先求P点所在法线
            f1 = 1/fuc_derivative(i, norm)
            a1 = f1
            b1 = -1
            c1 = py-f1*px
        #     求该点与上一个点的连线
            f2 = (real_arr[i] - real_arr[i-delta_x]) / delta_x
            a2 = f2
            b2 = -1
            c2 = real_arr[i] - f2*i
            qx, qy = get_cross_point(a1,b1,c1,a2,b2,c2)
            dis = point_dis(px,py,qx,qy)
        else:
            dis = real_arr[i] - fuc_sin_val(i,norm)
        dis_arr.append(dis)

    return np.array(dis_arr)

def old_dis(real_arr):
    dis_arr = []
    length = len(real_arr)
    norm = real_arr[0]
    for i in range(length):
        dis = real_arr[i] - fuc_sin_val(i,norm)
        dis_arr.append(dis)
    return np.array(dis_arr)

if __name__ == '__main__':
    k = 100
    n = 3
    real_val_columns = np.loadtxt('wavedata/real.txt')
    sin_val_columns = np.loadtxt('wavedata/sin.txt')
    # sub_val_columns = np.loadtxt('G:\\Desktop\\sub_val_columns.txt')
    x = list(range(k))
    # real_arr=list(real_val_columns[:k,n])
    # sin_arr=list(sin_val_columns[:k,n])
    # sub_arr=list(sub_val_columns[:k,n])

    # [-k:,n]表示第n列中从后往前数的第4700-k到第4700
    # real_arr=list(real_val_columns[-k:,n])
    real_arr = list(real_val_columns[0:k, n])

    # sin_arr=list(sin_val_columns[-k:,n])
    sin_arr = list(sin_val_columns[0:k, n])

    new_dis_arr = new_dis(np.array(real_arr))
    old_dis_arr = old_dis(np.array(real_arr))
    # sub_arr=list(sub_val_columns[-k:,n])
    # plt.plot(x,sin_arr,'g',x,real_arr,'r',x,sub_arr,'b')
    plt.plot(x,sin_arr,label="sin")
    plt.plot(x,real_arr,label="real")
    plt.plot(x,new_dis_arr,label='new')
    plt.plot(x,old_dis_arr,label='old')
    plt.legend()
    plt.savefig('test100.png')
    plt.show()