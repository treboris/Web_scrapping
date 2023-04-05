from bs4 import BeautifulSoup
from datetime import datetime
from tqdm import tqdm
import pandas as pd
import requests
import time
import os



with open('../initial.txt','r') as file:
    initial = int(file.read())

cond = False
text = ""
date = datetime.today().strftime('%Y-%m-%d')
data = pd.read_csv(f'../../../data/cvonline/cvonline{initial}.csv')



print(initial)
data_size = (data['ID'].size) -1
print(data_size)
href = data['Href'].to_list()



def conn(url_piece):
    url = (f"{url_piece}")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    return soup.body


for x in tqdm(range(0,data_size)):
    full_page = conn(href[x])

    with open(f"../../../data/txt/cvonline/{initial}/temp.txt" , "w") as f:
        f.write(full_page.text)
    with open(f"../../../data/txt/cvonline/{initial}/temp.txt" , "r") as f:
        for line in f:
            if(line.strip()):
                if ('ÁLLÁSHIRDETÉS FELADÁS' in line):
                    cond = True
                if (cond):
                    text += line

    with open(f"../../../data/txt/cvonline/{initial}/job{x}.txt" , "w") as f:
        f.write(text)


    text = ""
    os.remove(f"../../../data/txt/cvonline/{initial}/temp.txt")
    cond = False
