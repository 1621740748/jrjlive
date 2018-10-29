# -*- coding: UTF-8 -*- 
#c="c:\\download11\\财报分析:(九十二)年报看点二十:其他重要事项-视频频道-金融界.mp4";
c="c:\\download11\\财报分析:(九十二)年报看点二十:其他重要事项-视频频道-金融界.mp4";
c=c.replace(":","")
print(c)
f=open(c,"wb")
f.write("aaa")
f.close()