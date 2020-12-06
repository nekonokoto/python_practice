# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:15:01 2020

@author: micha
"""

import requests
import json
import urllib
import time
page=0
m=85
folder_path='E:/photo/'
for num in range(0,9):
    page=48*num
    s_page=str(page)
    imgs = requests.get(' https://pic.sogou.com/pics?query=fgo+%C3%C0%88%44&mode=1&start='+s_page+'&reqType=ajax&reqFrom=result&tn=0')
    jd = json.loads(imgs.text)
    jd = jd['items']
   
    for j in jd:
        print(j['pic_url'])
        k=str(m)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        try:
            urllib.request.urlretrieve(j['pic_url'],folder_path+k+'.jpg')
            print(k+'success')
            m+=1
            
            time.sleep(5)
            
        except Exception:
                print('error')
        pass
            