from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from tqdm import tqdm
import time
import pandas as pd
import os
import glob
recon = 0

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


def m():
    counter = 0
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options = options)
    text = ''
    data = pd.read_csv(f'../../../data/stepstone/stepstone{initial}.csv')
    data_size = (data['ID'].size) -1
    href = data['Href'].to_list()

    def conn(href):

        time.sleep(0.5)
        url = (f"{href}")
        return driver.get(url)

    def scrape(x):
        try:
            body = driver.find_element(By.XPATH,f'/html/body/div[2]/div[2]/div/div[1]/div/div[1]')
        except (NoSuchElementException):
            print('Reconnecting...')
            if(recon > 5):
                restart_browser()
            conn(href[x])
            time.sleep(3)
            recon +=1
            scrape(x)

        except selenium.common.exceptions.WebDriverException:
            print('Reconnecting...')
            if(recon > 5):
                restart_browser()
            conn(href[x])
            time.sleep(2)
            recon +=1
            scrape(x)
        return body.text

    for x in tqdm(range(file_count(),data_size)):

        if (counter >= 50):
            break
        else:
            conn(href[x])
            full_page = scrape(x)
            with open(f"../../../data/txt/stepstone/{initial}/temp.txt" , "w") as f: #read&write
                f.write(full_page)
                f.close()
            with open(f"../../../data/txt/stepstone/{initial}/temp.txt" , "r") as f:
                for line in f:
                    if(line.strip()):
                        text += line
            with open(f"../../../data/txt/stepstone/{initial}/job{x}.txt" , "w") as fil:
                fil.write(text)
            text = ""
            os.remove(f"../../../data/txt/stepstone/{initial}/temp.txt")
            counter += 1

csvnum = int(csv_count())
while(file_count() < csvnum):
    m()
    restart_browser()

print('\a')
