

from multiprocessing.dummy import Pool as ThreadPool
import urllib

from bs4 import BeautifulSoup

import os

import time
import lxml

import requests
from selenium import webdriver





chrome_path="E:\jrbook\chromedriver.exe"

web=webdriver.Chrome(chrome_path)

web.get('https://bbs.yamibo.com/member.php?mod=logging&action=login')

element_user=web.find_element_by_name('username')

element_user.send_keys('user')

element_pass=web.find_element_by_name('password')

element_pass.send_keys('password')

cookie=[]
commit = web.find_element_by_name('loginsubmit')

commit.click()
time.sleep(5)
cookie={}


web.maximize_window()
pool = ThreadPool(5)
urls=[]
folder=[]
x=50296






for i in range(1,50):
    
    x=x-1
    y=str(x)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    url='https://bbs.yamibo.com/thread-'+y+'-1-1.html'
    g=str(i) 
    folder_path='E:/pictures/'+y+'/'
   
        
       

    web.get(url)
    resw=web.find_elements_by_xpath("//div[@id='pt']//a")
    try:
    
        if resw[-2].text == '中文漫画区': 
            pos=0
            m=0
            if os.path.isdir(folder_path):
                 print("目錄存在。")
            else:
                 print("目錄不存在。")
                 os.makedirs('E:/pictures/'+y)
            
            for j in range(100):
                pos+=j*500
                js="document.documentElement.scrollTop=%d"%pos
                web.execute_script(js)
            time.sleep(5)
            z=1
            for element in web.find_elements_by_tag_name('img'):
                    img_url = element.get_attribute('src')
                  
                    if type(img_url) is str and (img_url.split('.')[-1]=='jpg' or img_url.split('.')[-1]=='png'):
                            urls.append(img_url)
                           
                            
                            
                            f=str(z+i)
                            
                            h=str(z)
                            z=z+1
                            folder.append(folder_path+h+'.jpg')
    
                        
                        
                        
                       
            try:
                
                pool.starmap(urllib.request.urlretrieve,zip(urls,folder))
                
        
                print(g+'success')
                time.sleep(10)
            except Exception as e:
                print(e)
            pass
        else:
           
            print('這裡沒有塗')
        pass
    except Exception as e:
        print(e)
    pass
# In[ ]:





# In[ ]:




