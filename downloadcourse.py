# -*- coding: UTF-8 -*- 
import requests;
import threading
import os
import json
import pycurl
s1=threading.Semaphore(5)
def downloadnotok(url,file):
    with open(file, 'wb') as f:
         c = pycurl.Curl()
         c.setopt(c.URL, url)
         c.setopt(c.WRITEDATA, f)
         c.perform()
         c.close()
                
def download(url,file):
    r1 = requests.get(url, stream=True, verify=False)
    total_size = int(r1.headers['Content-Length'])
    temp_size = 0
    # 这重要了，先看看本地文件下载了多少
    if os.path.exists(file):
        temp_size = os.path.getsize(file)  # 本地已经下载的文件大小
    else:
        temp_size = 0
    # 显示一下下载了多少   
    if temp_size!=total_size:
        print(file)
        downloadnotok(url, file)   
        

dir="g:\\course\\"
def downloadRun(url,name):
    s1.acquire()
    try:
        if name!=None:
            a=name+".mp4";
        else:
            a=url[url.rfind('/')+1:]    
        file=dir+a;
        print(file)   
        download(url,file)
    except IOError as e:
        print(e)
    s1.release()
file=open("a.txt","r",encoding="utf-8")
c=file.read()
js=json.loads(c)
l=[(a['flv_url'],a['teacher'])for a in js['data']]
threads=[]
for u,name  in l:
    try:
       t= threading.Thread(target=downloadRun,args=(u.strip(),name))
       threads.append(t)
       t.start()
    except IOError as e:
        print(e)
for t in threads:
    t.join()  
print("下载完成")         