from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
import pandas as pd
import requests
import time
import os


print("JOBLINE-scrapper STARTED")
start_time = time.time()

text = ""
date = datetime.today().strftime('%Y-%m-%d')
data = pd.read_csv('data/Jobline_2023-02-10.csv')

dataindex = data.index
data_size = len(dataindex)
href = data['Href'].to_list()


for x in tqdm(range(0,data_size)):
    url_piece = href[x]
    url = (f"https://jobline.hu{url_piece}")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    full_page = soup.body

    #exists = os.path.exists(f"txt/jobline_{date}/job{x}.txt")

    with open(f"txt/temp.txt" , "w") as f: #read&write
        f.write(full_page.text)
        f.close()
    with open(f"txt/temp.txt" , "r") as f:
        for line in f:
            if(line.strip()):
                text += line
    with open(f"txt/jobline/job{x}.txt" , "w") as fil:
        fil.write(text)
    text = ""
    os.remove("txt/temp.txt")
print("--- %s seconds ---" % (time.time() - start_time))
