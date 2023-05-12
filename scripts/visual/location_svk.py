import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import pandas as pd
import re

new_region = {}
region = {'Bratislava' : 0 , 'Nitra' : 0 ,'Košice': 0, 'Ružinov': 0 , 'Trenčín' : 0 , 'Žilina': 0,'Zvolen' : 0,
        'Abroad':0 , 'Poprad' : 0 ,'Prievidza' : 0, 'Brno' : 0 , 'Praha' : 0, 'Česko':0,'Rimavská Sobota' :0,'Prešov' : 0,
        'Dunajská Streda' : 0,'Liptovský Mikuláš' : 0 , 'Michalovce' : 0 ,'Banská Bystrica' : 0, 'Komárno' :0, 'Remote' :0,'Košický kraj' :0,
        'Bratislavský kraj' : 0}


def filter(list):
    filtered = [*set(list)]
    for f in filtered:
        print(f)
        pass
    return filtered

def remote_works(list):
    words = ['remote' , 'práca z domu','práce z domu','prácu z domu' , 'home office']
    for l in list:
        for w in words:
            pattern = re.search(f'{w.casefold()}',str(l).casefold())
            if(pattern):
                region['Remote'] +=1

def main(initial):
    data_professia = pd.read_csv(f'../../data/professia/professia{initial}.csv')
    location = data_professia['Location'].to_list()
    remote_works(location)

    for l in location:
        new_str = l.replace(',', '')
        for reg in region.keys():
            pattern = re.search(f'{reg.casefold()}',new_str.casefold())
            if(pattern):
                region[f'{reg}'] += 1

    data_kariera = pd.read_csv(f'../../data/kariera/kariera{initial}.csv')
    location_1  = data_kariera['Location'].to_list()
    remote_works(location_1)
    for lo in location_1:
        new_str = str(lo).replace(',', '')
        for reg in  region.keys():
            pattern = re.search(f'{reg.casefold()}',str(new_str).casefold())
            if(pattern):
                region[f'{reg}'] += 1


    for key , value in region.items():
        if value >20:
            new_region[key] = value


for x in range(0,3):
    try:
        main(x)
    except Exception as e:
        raise

df = pd.DataFrame(list(new_region.items()), columns=['city', 'count'])
df.to_csv('diagram_data/location_svk.csv', index=False)



print('\a')
