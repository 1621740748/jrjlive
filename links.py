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
    flag=os.path.exists(file)
    if flag:
        return;
    c=requests.get(url)
    f=open(file,'wb')
    f.write(c.content) 
    f.close()       
        
url="http://v.jrj.com.cn/2015-09-23/000000027276.shtml"

dir="c:\\download11\\"
def downloadRun(url):
    s1.acquire()
    try:
        a,b=geturl(url)
        print("title=",a)
        print("vurl=",b)  
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