from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
import pandas as pd
import requests
import time
import os
from tqdm import tqdm


print("PROFESSIA.SK-page STARTED")

text = ""
initial = 2
date = datetime.today().strftime('%Y-%m-%d')
data = pd.read_csv(f'../data/professia/professia{initial}.csv')

dataindex = data.index
data_size = len(dataindex)
href = data['Href'].to_list()

def lost_data():
    with open(f"../txt/professia/{initial}/job{x}.txt" , "w") as fil:
        fil.write(text)



for x in tqdm(range(0,data_size)):
    url_piece = href[x]
    url = (f"https://www.profesia.sk{url_piece}")
    try:
        page = requests.get(url, timeout = 5)
        soup = BeautifulSoup(page.text,"html.parser")
        full_page = soup.body
        with open(f"../txt/professia/{initial}/temp.txt" , "w") as f: #read&write
            f.write(full_page.text)
        with open(f"../txt/professia/{initial}/temp.txt" , "r") as f:
            for line in f:
                if(line.strip()):
                    text += line
        with open(f"../txt/professia/{initial}/job{x}.txt" , "w") as fil:
            fil.write(text)
        text = ""
    #TIMEOUT NO INTERNET CONNECTION
    except requests.exceptions.Timeout:
        lost_data(x)
        text = ''
    #CAN'T CONNECT BAD URL
    except requests.exceptions.ConnectionError:
        lost_data(x)
        text = ''
    #TIMEOUT NO INTERNET CONNECTION OR BAD URL
    except requests.exceptions.ReadTimeout:
        lost_data(x)
        text = ''
    #TIMEOUT NO INTERNET CONNECTION OR BAD URL
    except requests.exceptions.ConnectTimeout:
        lost_data(x)
        text = ''
    os.remove(f"../txt/professia/{initial}/temp.txt")
