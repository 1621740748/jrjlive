# -*- coding: UTF-8 -*- 
import requests;
import re
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
url="http://v.jrj.com.cn/2015-09-23/000000027276.shtml"
a,b=geturl(url)
print("title=",a)
print("vurl=",b)    