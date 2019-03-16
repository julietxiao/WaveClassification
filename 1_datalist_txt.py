'''
    将文件夹中所有文件的文件名都写入1_datalist.txt文件中，便于读取遍历；
'''
import os
 
def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    file.write(name + "\n")
                    break
 
def Test():
    dir="G:/Desktop/风机/code/2号机/"                     #文件路径
    outfile="G:/Desktop/风机/code/1_datalist.txt"         #写入的txt文件名
    wildcard = ".dat "      #要读取的文件类型；
 
    file = open(outfile,"w")
    if not file:
       print ("cannot open the file %s for writing" % outfile)
    
    ListFilesToTxt(dir,file,wildcard, 1)
    file.close()
Test() 
