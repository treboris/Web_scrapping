from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
from datetime import datetime
from tqdm import tqdm
from modules.Data import Save
import modules.tools as tools
import pandas as pd
import time
import requests




initial = tools.initial()
exists = tools.f_exists('jobline',initial)

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
date = datetime.today().strftime('%Y-%m-%d')

id = []
main = []
href = []
corp = []
location = []
datee = []

#CONNECTION
def conn(limit):
    url = (f"https://jobline.hu/allasok/it_telekommunikacio-teljes_munkaido?p={limit}")
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    return soup

#GET-PAGE-NUMBER
def page_number():
    url = (f"https://jobline.hu/allasok/it_telekommunikacio-teljes_munkaido?p=1")
    page = requests.get(url)
    soup_number = BeautifulSoup(page.text,"html.parser")
    page_number = soup_number.find('h4', class_='align_center')
    string_split = (page_number.text).split()
    max_page_number = round(int(string_split[0])/20)
    return max_page_number


for limit in tqdm(range(0,page_number())):

    main_tag = conn(limit).find_all('div',class_='job-main')
    corp_tag = conn(limit).find_all('div',class_='job-info')

#location & main
    for m in main_tag:
        m_ = m.text.replace("\n","")
        m_list = m_.split()
        loc = m.text.split()
        del m_list[-1]
        m_text = " ".join(m_list)
        location.append((loc[-1].replace("(","")).replace(")",""))
        main.append(m_text)

#corporation
    for c in corp_tag:
        c_ = c.text.replace("\n","")
        corp.append(c_)

#HREF EXTRACT
    for div in conn(limit).find_all('div' , class_='center'):
            for link in div.find_all('article'):
                for a in link.find_all('a' , class_='l-cta_button open job-material-click'):
                    href.append(a.get('href'))
driver.close()

#ID
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)

save_data = Save('jobline',f'jobline{initial}' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp) , ("Href" , href),("Date" , datee) )
