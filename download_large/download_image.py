# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:03:49 2020

@author: micha
"""
import requests

import urllib.request

from bs4 import BeautifulSoup

import os

import time
url='https://www.google.com/search?q=fgo+%E7%BE%8E%E5%9C%96&sxsrf=ACYBGNSsVXm-Z5KUAyaHR-hwXQQrWARbdQ:1581853029593&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-vKnf_dXnAhWlNKYKHcoGC5kQ_AUoAXoECAsQAw&biw=1536&bih=760'
photolimit=10

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url,headers = headers) #使用header避免訪問受到限制

soup = BeautifulSoup(response.content, 'html.parser')

items = soup.find_all('img')

folder_path ='./photo/'

if (os.path.exists(folder_path) == False): #判斷資料夾是否存在

    os.makedirs(folder_path) #Create folder



for index , item in enumerate (items):

    if (item and index < photolimit ):

        html = requests.get(item.get('src')) # use 'get' to get photo link path , requests = send request

        img_name = folder_path + str(index + 1) + '.png'



        with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入

            file.write(html.content)

            file.flush()

        file.close() #close file

        print('第 %d 張' % (index + 1))

        time.sleep(1)



print('Done')

