# -*- coding: UTF-8 -*- 
import json
file=open("a.txt","r",encoding="utf-8")
c=file.read()
js=json.loads(c)
l=[(a['flv_url'],a['teacher'])for a in js['data']]
print(l)
s='http://flv.jrj.com.cn/src_video/20180327/27c7d401192f9445bca491a4c4fa9ff1/GQ/5ab9939c52fea.mp4'
print(s[s.rfind('/')+1:])