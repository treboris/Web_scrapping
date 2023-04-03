from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
from tqdm import tqdm
import requests
import time
import re

start_time = time.time()
date = datetime.today().strftime('%Y-%m-%d')

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)

limit_txt = "?page_num="

id = []
corp = []
main = []
location = []
href = []
salary = []
datee =[]

def page_number():
    url = (f"https://www.profesia.sk/praca/programator/{limit_txt}{limit}")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    number = soup.find('div',class_='offer-counter text-right bold')
    splitted = number.text.split()
    return(int(splitted[-1]))

limit = 1

def conn(limit_txt,limit):
    url = (f"https://www.profesia.sk/praca/programator/{limit_txt}{limit}")
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    return soup

page = round(float(page_number()/20))

for limit in tqdm(range(page)):

    main_block = conn(limit_txt,limit).find('ul', class_='list')

    for li in main_block.select('.list-row:has(div)'):
        for h2 in li.find_all('h2'):
            for a in h2.find_all('a'):
                href.append(a.get('href'))
        for title in li.find_all('span',class_='title'):
            main.append(title.text)
        try:
            for loc in li.find_all('span',class_='job-location'):
                location.append(loc.text)
        except (AttributeError,TypeError):
                location.append("None")
        for corporation in li.find_all('span',class_='employer'):
            corp.append(corporation.text)

    for x in range(1,21):
        try:
            label = driver.find_element(By.XPATH,f"//*[@id='content']/div/div/main/div/ul/li[{x}]/span[3]")
            splitted = (label.text).split()
            if('Od' in splitted):
                splitted.remove('Od')
            if('Можливість' in splitted):
                splitted.remove('Можливість')
                splitted.remove('для')
                splitted.remove('людей')
                splitted.remove('України')
            if('Reagujte' in splitted):
                splitted.remove('Reagujte')
                splitted.remove('bez')
                splitted.remove('životopisu')
            if('Ponuka' in splitted):
                splitted.remove('Ponuka')
                splitted.remove('onedlho')
                splitted.remove('končí!')
            if('з' in splitted):
                splitted.remove('з')
            salary.append(" ".join(splitted))
        except (NoSuchElementException):
            salary.append("None")
driver.quit()

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)

save_data = Save(f'professia1' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp),("Salary" , salary) , ("Href" , href),("Date" , datee) )
