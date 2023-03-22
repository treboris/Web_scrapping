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
def scrape():
    try:
        article = driver.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]')
        href_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[2]/a')
        #print(href_tag.get_attribute('href'))
        href.append(href_tag.get_attribute('href'))

        main_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[2]/a/div/div/div')
        main.append(main_tag.text)
        corp_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[3]/span')
        corp.append(corp_tag.text)
        location_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[4]/div[1]/div[1]/span/span')
        location.append(location_tag)
        save_data = Save(f'stepstone1' , ("Main" , main) ,("Location" , location), ("Corporation" , corp), ("Href" , href) )

    except (NoSuchElementException):
        print('Reconnecting...')
        conn(limit)
        time.sleep(2)
        scrape()


for limit in tqdm(range(page_number())):
    conn(limit)
    time.sleep(2)
    for x in range(1,26):
        scrape()

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)





print(f'{len(corp)},{len(main)},{len(location)},{len(href)}')





driver.quit()
