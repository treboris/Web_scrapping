from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import time
import requests

print("Script STARTED")
start_time = time.time()


options = Options()
options.headless = True


driver = webdriver.Firefox(options = options)



####################################PROFESSION#####################################
#CSAK A HIRDETES CIMET AZ ALCIMKEKET ES A CEG NEVET HELYSZINT SCRAPPELI



upload_date = []
corp = []
main = []
labels = []
location = []



#PAGE COUNTER
url = (f"https://www.profession.hu/allasok/it-programozas-fejlesztes/1,10,0,0,200_201_393_448_75_76_202_363_450_80_449")
page = requests.get(url)
soup_number = BeautifulSoup(page.text,"html.parser")
page_number = soup_number.find(id='jobs_block_count')
string_split = (page_number.text).split()
max_page_number = round(int(string_split[0])/20)
print(f"Jobs: {string_split[0]}")
print(f"Pages to scrap: {max_page_number}")

i = 0
while i < max_page_number:
    url = (f"https://www.profession.hu/allasok/it-programozas-fejlesztes/{i},10,0,0,200_201_393_448_75_76_202_363_450_80_449")
    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html,"html.parser")

    main_tag = soup.find_all('a' class_"title")
    for main in main_tag:
        print(main.text)



    i += 1
driver.quit()
