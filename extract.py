# -*- coding: UTF-8 -*- 
import re
file=open("urls.txt","r")
filew=open("u.txt","w")
c=file.read()
file.close()
r=r'<a href="(.*)">';
all=re.findall(r, c)
for u in all:
    filew.write(u+"\n")
filew.close();