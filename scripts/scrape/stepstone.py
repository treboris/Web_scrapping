from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
from tqdm import tqdm
import requests
import socket
import time
import re

#hostname = socket.gethostname()
#my_ip = socket.gethostbyname(hostname)
#print(f'{hostname},{my_ip}')

#https://github.com/ultrafunkamsterdam/undetected-chromedriver

initial = 1
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
date = datetime.today().strftime('%Y-%m-%d')

id = []
corp = []
main = []
location = []
href = []
datee =[]


def page_number():
    url = (f"https://www.stepstone.de/work/it?page=1&fdl=en")
    driver.get(url)
    number = driver.find_element(By.XPATH,f"/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/nav/ul/li[8]/a/span/span/span")
    return int(number.text)

#/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[1]

def conn(limit):
    url = (f"https://www.stepstone.de/work/it?page={limit}&fdl=en")
    return driver.get(url)


#REKURZIV FUGGVENY
def scrape(x):
    try:
        article = driver.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]')
        href_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[2]/a')
        to_str = href_tag.get_attribute('href')
        href.append(to_str)
        main_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[2]/a/div/div/div')
        main.append(main_tag.text)
        corp_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[3]/span')
        corp.append(corp_tag.text)
        location_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[4]/div[1]/div[1]/span/span')
        location.append(location_tag.text)
    except (NoSuchElementException):
        print('Reconnecting...')
        conn(limit)
        time.sleep(2)
        scrape(x)
print("star")
for limit in tqdm(range(page_number())):
    conn(limit)
    time.sleep(2)
    for x in range(1,26):
        scrape(x)

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)

save_data = Save('stepstone',f'stepstone{initial}' ,('ID' , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp), ("Href" , href),('Date' , datee) )
driver.quit()
print('\a')
