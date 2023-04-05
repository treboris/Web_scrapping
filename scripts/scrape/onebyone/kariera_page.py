from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
import pandas as pd
import requests
import time
import os

with open('../initial.txt','r') as file:
    initial = int(file.read())

text = ""
date = datetime.today().strftime('%Y-%m-%d')
data = pd.read_csv(f'../../../data/kariera/kariera{initial}.csv')

data_size = data.size
href = data['Href'].to_list()

for x in range(0 , data_size):
    url_piece = href[x]
    url = (f"https://kariera.zoznam.sk/{url_piece}")
    try:
        page = requests.get(url, timeout = 5)
        soup = BeautifulSoup(page.text,"html.parser")
        full_page = soup.body
        try:
            with open(f"../../../data/txt/kariera/{initial}/temp.txt" , "w") as f: #read&write
                f.write(full_page.text)
            with open(f"../../../data/txt/kariera/{initial}/temp.txt" , "r") as f:
                for line in f:
                    if(line.strip()):
                        text += line
            with open(f"../../../data/txt/kariera/{initial}/job{x}.txt" , "w") as file:
                file.write(text)
            text = ''
            os.remove(f"../../../data/txt/kariera/{initial}/temp.txt")

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
