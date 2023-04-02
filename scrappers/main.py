from one_by_one_scrape import *
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import requests
import os

web_pages = ['profession' ]
initial = 1

#WEBSCRAPING JOBS ONE BY ONE

for x in tqdm(range(0,len(web_pages))):
    data = pd.read_csv(f'data/{web_pages[x]}/{web_pages[x]}{initial}.csv')
    href = data['Href'].to_list()
    name = web_pages[x]+str(initial)
    for y in tqdm(range(0,size(f'{web_pages[x]}',f'{name}.csv'))):
        file_write(web_pages[x],href[y] ,y,int(initial))

    href = []