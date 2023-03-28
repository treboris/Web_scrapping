from bs4 import BeautifulSoup
from datetime import datetime
from tqdm import tqdm
import pandas as pd
import requests
import time
import os


start_time = time.time()
cond = False
text = ""
date = datetime.today().strftime('%Y-%m-%d')
data = pd.read_csv('../data/Cvonline_2023-03-04.csv')
initial = 3


dataindex = data.index
data_size = len(dataindex)
href = data['Href'].to_list()



def conn(url_piece):
    url = (f"{url_piece}")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    return soup.body


for x in tqdm(range(0,data_size)):
    full_page = conn(href[x])


    with open(f'../txt/cvonline/{initial}/soup/soup{x}.html','w') as f:
        f.write(full_page.prettify())
    with open(f"../txt/cvonline/{initial}/temp.txt" , "w") as f:
        f.write(full_page.text)
    with open(f"../txt/cvonline/{initial}/temp.txt" , "r") as f:
        for line in f:
            if(line.strip()):
                if ('ÁLLÁSHIRDETÉS FELADÁS' in line):
                    cond = True
                if (cond):
                    text += line

    with open(f"../txt/cvonline/{initial}/job{x}.txt" , "w") as f:
        f.write(text)


    text = ""
    os.remove(f"../txt/cvonline/{initial}/temp.txt")
    cond = False
