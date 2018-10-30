# -*- coding: UTF-8 -*- 
import requests;
import re
import threading
import os
s1=threading.Semaphore(15)
def geturl( url):
    c=requests.get(url)
    #print(c.content)
    title=""
    vurl=""
    titleO=re.search(r'<title>(.*)</title>',c.text)
    if titleO:
        #print(titleO.group(1))
        title=titleO.group(1)
    videoUrlO=re.search(r'var videoURL = "(http://.*)"',c.text)    
    if videoUrlO:
        #print(videoUrlO.group(1))
        vurl=videoUrlO.group(1)
    return (title,vurl)
def download(url,file):
    r1 = requests.get(url, stream=True, verify=False)
    total_size = int(r1.headers['Content-Length'])

    # 这重要了，先看看本地文件下载了多少
    if os.path.exists(file):
        temp_size = os.path.getsize(file)  # 本地已经下载的文件大小
    else:
        temp_size = 0
    # 显示一下下载了多少   
    if temp_size!=total_size:
        print(file)
    #c=requests.get(url)
    #f=open(file,'wb')
    #f.write(c.content) 
    #f.close()       
        

dir="c:\\download11\\"
def downloadRun(url):
    s1.acquire()
    try:
        a,b=geturl(url)
#        print("title=",a)
#        print("vurl=",b) 
        a=a.replace(":","")
        a=a.replace("?","")
        file=dir+a+".mp4"
        download(b,file)
    except IOError as e:
        print(e)
    s1.release()
f=open("u.txt","r")
list=f.readlines();
print(list)
threads=[]
for u  in list:
    try:
       t= threading.Thread(target=downloadRun,args=(u.strip(),))
       threads.append(t)
       t.start()
    except IOError as e:
        print(e)
for t in threads:
    t.join()  
print("下载完成")         