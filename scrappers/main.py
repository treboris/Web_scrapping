from one_by_one_scrape import *
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import requests
import os





web_pages = ['cvonline','itpeople' ,'jobline','kariera','professia' , 'profession' ]
initial = 0

index = 5





#WEBSCRAPING JOBS ONE BY ONE

for x in tqdm(range(1,len(web_pages))):
    data = pd.read_csv(f'data/{web_pages[index]}{initial}.csv')
    href = data['Href'].to_list()
    name = web_pages[index]+str(initial)
    for y in tqdm(range(0,size(f'{name}.csv'))):
        file_write(web_pages[index],href[y] ,y,int(initial))


    href = []
    index+=1
