# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:33:39 2020

@author: micha
"""

import requests

res = requests.get('https://portal.ncu.edu.tw/login;jsessionid=55B02443FDF9A13FE39823A774880C77')
print(res.text)