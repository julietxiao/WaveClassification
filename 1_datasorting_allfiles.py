'''
	删除《2号机》每个文件中的无用数据（前43行和前两列后三列）
'''
import os
import pandas as pd 
import numpy as np 

res=r'G:\\Desktop\\风机\\code\\2号机\\'          		#处理前原始所有dat文件所在的文件夹
list = r'G:\\Desktop\\风机\\code\\1_datalist.txt' 		 #dat数据名字汇总txt
savePath=r'G:\\Desktop\\风机\\code\\1_datasorting_allfiles\\'  		 #处理后保存所有dat文件所在的文件夹

f = open(list,'r')							#从汇总txt逐个读取原始文件
lines = f.readlines()
for line in lines[:]:
	name = line.strip()
	resfile=res+name 				  			#每次要处理的dat文件路径
	openFileHandle=open(resfile,'r')
	savefile=savePath+name[:-4]+'.txt'			#每次处理后的txt文件保存路径
	writeFileHandle=open(savefile,'w') 

	for line in openFileHandle.readlines()[43:]: #删去原始文件中无用的前42行
  		writeFileHandle.write(line)
  	
openFileHandle.close()
writeFileHandle.close()
	
for line in lines[:]:						#从汇总txt逐个读取处理后的文件
	name = line.strip()
	savefile=savePath+name[:-4]+'.txt'
	a=np.loadtxt(savefile) 						 #删去原始文件中无用的列(前两列和后两列)
	a=np.around(a[:,2:-3],decimals=2)
	np.savetxt(savefile,a,fmt="%.2f")
