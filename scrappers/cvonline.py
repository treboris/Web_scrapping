from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
from tqdm import tqdm
from Data import Save
import pandas as pd
import re
import os

import time
import requests




print("CVONLINE.hu-scrapper STARTED")
start_time = time.time()
date = datetime.today().strftime('%Y-%m-%d')

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)


limit_txt = "?page="
location = []
href = []
datee =[]
corp = []
main = []
id = []




#CONNECTION
def conn(limit_txt,limit):
    url = (f"https://www.cvonline.hu/hu/allashirdetesek/it-informatika-0{limit_txt}{limit}")
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    return soup


#GET-PAGE-NUMBER
def page_number():
    url = (f"https://www.cvonline.hu/hu/allashirdetesek/it-informatika-0")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    number = soup.find('h1', class_= 'search-result-header')
    splitted = number.text.split()
    return splitted[0]

max_page_number = round(int(page_number()) / 20)

for limit in tqdm(range(max_page_number)):
    fblock = conn(limit_txt,limit).find('div' , class_='l-content')

    for h2 in fblock.find_all('h2', class_='node__title'):
        strip = h2.text.strip()
        strip = re.sub('\n',"",strip)
        main.append(strip)
        for a in h2('a'):
            href.append(a.get('href'))

    for span in fblock.find_all('span', class_='recruiter-company-profile-job-organization'):
        corp.append(span.text)


    job = fblock.find_all('div' , class_= 'job__content clearfix')
    for element in job:
        loc = element.find('div' , class_= 'location')
        try:
            for l in loc.find('span'):
                location.append(l.text)
        except (AttributeError,TypeError):
                location.append(None)


driver.quit()


#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)




save_data = Save(f'Cvonline_{date}' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp) , ("Href" , href),("Date" , datee) )


#TO TXT










print("Execution time: %s seconds ---" % (time.time() - start_time))
