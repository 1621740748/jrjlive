# -*- coding: UTF-8 -*- 
import requests;
import re
import threading
import os
s1=threading.Semaphore(15)
def downloadnotok(url,file,start):
        # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载
    headers = {'Range': 'bytes=%d-' % start}  
    # 重新请求网址，加入新的请求头的
    r = requests.get(url, stream=True, verify=False, headers=headers)

    # 下面写入文件也要注意，看到"ab"了吗？
    # "ab"表示追加形式写入文件
    with open(file, "ab") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                start += len(chunk)
                f.write(chunk)
                f.flush()
                
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
    temp_size = 0
    # 这重要了，先看看本地文件下载了多少
    if os.path.exists(file):
        temp_size = os.path.getsize(file)  # 本地已经下载的文件大小
    else:
        temp_size = 0
    # 显示一下下载了多少   
    if temp_size!=total_size:
        print(file)
        downloadnotok(url, file, temp_size)
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