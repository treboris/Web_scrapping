from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm
import time
import pandas as pd
import os




options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
initial = 1
text = ''


data = pd.read_csv(f'../data/stepstone/stepstone{initial}.csv')
data_size = (data['ID'].size) -1
href = data['Href'].to_list()




def conn(href):
    url = (f"{href}")
    return driver.get(url)



def scrape():
    try:
        body = driver.find_element(By.XPATH,f'/html/body/div[2]/div[2]/div/div[1]/div/div[1]')
    except (NoSuchElementException):
        print('Reconnecting...')
        conn(limit)
        time.sleep(2)
        scrape(x)


    return body.text




for x in tqdm(range(132,data_size)):
    conn(href[x])
    full_page = scrape()



    with open(f"../txt/stepstone/{initial}/temp.txt" , "w") as f: #read&write
        f.write(full_page)
        f.close()
    with open(f"../txt/stepstone/{initial}/temp.txt" , "r") as f:
        for line in f:
            if(line.strip()):
                text += line
    with open(f"../txt/stepstone/{initial}/job{x}.txt" , "w") as fil:
        fil.write(text)
    text = ""
    os.remove(f"../txt/stepstone/{initial}/temp.txt")
print('\a')
