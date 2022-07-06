# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 13:18:34 2022

@author: TalhaSoftware
"""


import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time


browser = webdriver.Firefox()

#"https://www.amazon.ca/s?me=ARJCJ2QPOLW53&marketplaceID=A2EUQ1WTGCTBG2"
url = input("Magaza url : ")

browser.get(url)

source = browser.page_source

soup = BeautifulSoup(source,"lxml")
    


kacsayfa = soup.find_all("span",{"class":"s-pagination-item s-pagination-disabled"})[0].text


asinler = []
page=0

kactane = int(kacsayfa)
if(kactane>176):
    kactane = 177
else:
    pass

while(page<int(kacsayfa)):
    
    page += 1
    
    if(page%15 == 0):
        browser.quit()
        browser = webdriver.Firefox()
    
    url= url + "&page=" + str(page)
    
    SCROLL_PAUSE_TIME = 2
    
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(SCROLL_PAUSE_TIME)
    except:
        pass
    
    source= browser.page_source
    
    
    soup = BeautifulSoup(source,"lxml")
    
    try:
        browser.execute_script("location.href='"+url+"';")
    except:
        browser.get(url)
    
    try:
        kutu1 = soup.find_all("a",{"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"},href=True)
    except:
        pass
    
   
    
    for i in kutu1:
        asinler.append(i["href"].split("/")[3])
        print(i["href"].split("/")[3])





textfile = open("ciktiisim.txt", "w")
for element in asinler:
    textfile.write(element + "\n")
textfile.close()







