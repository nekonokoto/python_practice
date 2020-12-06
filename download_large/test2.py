# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:48:08 2020

@author: micha
"""

import requests
from bs4 import BeautifulSoup
import lxml
import os
import urllib
import sys


r1=requests.get('https://www.douban.com/') #豆瓣網站
soup=BeautifulSoup(r1.text,'lxml')
image=soup.find_all('div')


#下面的迴圈是找圖片網址再把結果放到陣列裡
links=[]
for d in image:
	if d.find('img'):        #再從div找img裡面的src  
		result=d.find('img')['src']
		print (result)
		links.append(result)
x=1
for link in links:
    
	local = os.path.join('D:\py\musicplayer\webcrawler save\image\%s.jpg' % x)
	urlretrieve(link,local) #link是下載的網址 local是儲存圖片的檔案位址
	x+=1