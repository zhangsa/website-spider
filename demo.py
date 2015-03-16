# -*- coding: utf-8 -*-
#提取网页中的URL
import re
#第一次从前边匹配
a=re.compile('(http://.*?\.(?:xls|html))')
f=open('a.htm')
fileHandle = open ('F:\\out.txt','w') 
for i in f :
	res=a.findall(i)

for l in res :
    fileHandle.write(l+'\n') 
f.close()
fileHandle.close() 


#第二次从后边匹配

a=re.compile('((?:slx|lmth)\..*?//:ptth)')
f=open('F:\\out.txt')
fileHandle = open ('F:\\out2.txt','w') 
for i in f :
	res=a.findall(i[::-1])
	fileHandle.write(res[0][::-1]+'\n')
f.close()
fileHandle.close() 
