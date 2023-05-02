from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from tqdm import tqdm
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
import glob

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
text = ''
requests = 0

#AZ INITIAL VÁLTOZÓ INICIALIZÁLÁSA
with open('../initial.txt','r') as file:
    initial = int(file.read())


#CSV FÁJL BEOLVASÁSA
data = pd.read_csv(f'../../../data/stepstone/stepstone2.csv')

#SOROK SZÁMA A CSV FÁJLBAN
data_size = (data['ID'].size) -1

#A HIVATKOZÓ LINKET LISTÁBA SZÚRÁSA
href = data['Href'].to_list()




#BÖNGÉSZŐ ÚJRAINDÍTÁSA
def restart_browser():
    os.system('pkill firefox')

#FÁJL SZÁMLÁLÁS
def file_count():
    last_file_num = len(glob.glob1(f'../../../data/txt/stepstone/{initial}','*.txt'))
    return int(last_file_num)

#CSV FÁJL SOROK SZÁMA
def csv_count():
        data = pd.read_csv(f'../../../data/stepstone/stepstone{initial}.csv')
        return (data['ID'].size) -1

#CSATLAKOZÁST BIZTOSÍTÓ FÜGGVÉNY
def conn(href,attempts=0):
    global requests
    requests += 1
    url = (f"{href}")
    if (requests == 50):
        restart_browser()
        time.sleep(5)
    else:
        try:
            driver.get(url)
            time.sleep(2)
            html = driver.page_source
            soup = BeautifulSoup(html,"html.parser")
        except(NoSuchElementException):
            if (attempts == 5):
                restart_browser()
                time.sleep(5)
            else:
                attempts +=1
                time.sleep(5)
                conn()
        return soup
    raise AttributeError()




#FŐ CIKLUS
for x in tqdm(range(file_count(),data_size)):
    try:
        full_page = conn(href[x]).find('div',class_='js-app-ld-ContentBlock')
        with open(f"../../../data/txt/stepstone/{initial}/temp.txt" , "w") as f: #read&write
            f.write(full_page.text)
        with open(f"../../../data/txt/stepstone/{initial}/temp.txt" , "r") as f:
            for line in f:
                if(line.strip()):
                    text += line
        with open(f"../../../data/txt/stepstone/{initial}/job{x}.txt" , "w") as fil:
            fil.write(text)
        text = ""
        os.remove(f"../../../data/txt/stepstone/{initial}/temp.txt")
    except (TypeError,AttributeError):
        print('Browser restart.')
