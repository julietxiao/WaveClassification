'''
	删除 20150824190534Record.dat 文件中的无用数据（前43行和前两列后三列）
'''
import os
import numpy as np

openFileHandle=open('G:\\Desktop\\20150824190534Record.dat','r')
savafile='G:\\Desktop\\data.txt'
writeFileHandle=open(savafile,'w') 

for line in openFileHandle.readlines()[43:]: #删去原始文件中无用的前42行
  	writeFileHandle.write(line)

openFileHandle.close()
writeFileHandle.close()
a=np.loadtxt(savafile)						 #删去原始文件中无用的列(前两列和后两列)
print(a.shape)
b=np.around(a[:,2:-3],decimals=2)
np.savetxt('G:\\Desktop\\data1.txt',b,fmt="%.2f")
print(b.shape)
