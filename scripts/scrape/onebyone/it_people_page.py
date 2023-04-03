from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
from tqdm import tqdm
import pandas as pd
import requests
import time
import os


start_time = time.time()

text = ''
initial = 2
date = datetime.today().strftime('%Y-%m-%d')
data = pd.read_csv('../data/itpeople/itpeople1.csv')

dataindex = data.index
data_size = len(dataindex)
print
href = data['Href'].to_list()

def lost_data():
    with open(f"../txt/itpeople/{initial}/job{x}.txt" , "w") as file:
        file.write(text)

for x in tqdm(range(0,data_size)):
    url_piece = href[x]
    url = (f"{url_piece}")
    try:
        page = requests.get(url, timeout = 5)
        soup = BeautifulSoup(page.text,"html.parser")
        full_page = soup.body
        try:
            with open(f"../txt/itpeople/{initial}/temp.txt" , "w") as f: #read&write
                f.write(full_page.text)
            with open(f"../txt/itpeople/{initial}/temp.txt" , "r") as f:
                for line in f:
                    if(line.strip()):
                        text += line
            with open(f"../txt/itpeople/{initial}/job{x}.txt" , "w") as file:
                file.write(text)
            text = ''
            os.remove(f"../txt/itpeople/{initial}/temp.txt")

        except (AttributeError):
            lost_data()
            text = ''
    #TIMEOUT NO INTERNET CONNECTION
    except requests.exceptions.Timeout:
        lost_data()
        text = ''
    #CAN'T CONNECT BAD URL
    except requests.exceptions.ConnectionError:
        lost_data()
        text = ''
    #TIMEOUT NO INTERNET CONNECTION OR BAD URL
    except requests.exceptions.ReadTimeout:
        lost_data()
        text = ''
    #TIMEOUT NO INTERNET CONNECTION OR BAD URL
    except requests.exceptions.ConnectTimeout:
        lost_data()
        text = ''
