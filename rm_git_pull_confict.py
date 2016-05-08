#!/user/bin/python
# -*- coding:utf-8 -*-
import os 
import os.path 

#获取当前目录的完整路径
homedir = os.getcwd()

#把git pull的冲突文件导出到conflict.txt中
os.system("git pull > conflict.txt 2>&1;")

#判断conflict.txt是否存在，如果存在，变量赋值，否则为空
if os.path.exists("conflict.txt"): 
  conflict_file = open('conflict.txt','r')
else:
  conflict_file = None
  print ('there is no conflict.txt file')

#删除指定目录文件函数
def removeFileInFile(dir,targetFile): 
    if os.path.exists(dir + '/' + targetFile): 
        os.remove(dir + '/' + targetFile)
    else:
        print ('no such file:%s' % dir + targetFile)

#while循环，从conflict.txt中按行读取，如果这一行是一个文件，则删除它，如果不是执行下一个
#当读到行尾后，跳出while循环
while 1:
    if conflict_file != None:
        target_line = conflict_file.readline()
        target_line = target_line.strip()
        if not target_line:
            break
        #print target_line
        #print homedir + target_line
        if os.path.isfile(target_line):
            removeFileInFile(homedir , target_line)
        else:
            continue

if os.path.exists("conflict.txt"):
    os.remove("conflict.txt")

os.system("git pull")