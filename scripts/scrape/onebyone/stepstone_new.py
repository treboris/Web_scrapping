from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from tqdm import tqdm
from bs4 import BeautifulSoup
import requests

import time
import pandas as pd
import os
import glob


with open('../initial.txt','r') as file:
    initial = int(file.read())



def restart_browser():
    os.system('pkill firefox')


def file_count():
    last_file_num = len(glob.glob1(f'../../../data/txt/stepstone/{initial}','*.txt'))
    return int(last_file_num)


def csv_count():
        data = pd.read_csv(f'../../../data/stepstone/stepstone{initial}.csv')
        return (data['ID'].size) -1

def conn(href):

    url = (f"{href}")
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    return soup


options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
text = ''
data = pd.read_csv(f'../../../data/stepstone/stepstone{initial}.csv')
data_size = (data['ID'].size) -1
href = data['Href'].to_list()


for x in tqdm(range(file_count(),data_size)):
    try:
        full_page = conn(href[x]).find('div',class_='js-app-ld-ContentBlock')
    except (TypeError,AttributeError):
        print("ERROR")
    with open(f"../../../data/txt/stepstone/{initial}/temp.txt" , "w") as f: #read&write
        f.write(full_page.text)
        f.close()
    with open(f"../../../data/txt/stepstone/{initial}/temp.txt" , "r") as f:
        for line in f:
            if(line.strip()):
                text += line
    with open(f"../../../data/txt/stepstone/{initial}/job{x}.txt" , "w") as fil:
        fil.write(text)
    text = ""
    os.remove(f"../../../data/txt/stepstone/{initial}/temp.txt")
