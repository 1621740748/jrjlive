# -*- coding: UTF-8 -*- 
import json
import os
file=open("a.txt","r",encoding="utf-8")
c=file.read()
js=json.loads(c)
l=[(a['flv_url'],a['teacher'])for a in js['data']]
print(l)
s='http://flv.jrj.com.cn/src_video/20180327/27c7d401192f9445bca491a4c4fa9ff1/GQ/5ab9939c52fea.mp4'
print(s[s.rfind('/')+1:])
for u,f in l:
    path="g:\\course\\course\\"+u[u.rfind('/')+1:]
    if f!=None  and os.path.exists(path):
        path2="g:\\course\\course\\"+f.strip()+".mp4";
        print(path)
        print(path2)
        os.rename(path,path2)
        