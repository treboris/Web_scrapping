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

kraji = {'Bratislavský': 0 , 'Košický' : 0  , 'Nitriansky' : 0 , 'Banskobystrický' : 0}


def filter(list):
    filtered = [*set(list)]
    for f in filtered:
        print(f)
        pass
    return filtered

def add_labels():
    labels = []
    for x in new_region.values():
        labels.append(x)
    for i in range(len(labels)):
        plt.text(i, labels[i], labels[i], ha = 'center')

def barchart():
    fig, ax = plt.subplots(layout='constrained')
    fig.set_figheight(15)
    fig.set_figwidth(15)
    data = new_region
    add_labels()
    plt.title("Feladott hirdetések települések szerint")
    ax.set_title('Települések')
    ax.bar(*zip(*data.items()), color=['brown' , 'darkolivegreen','steelblue' , 'chocolate'],label = 'Sine')
    ax.set_ylim(0, 2200)
    ax.set_ylabel('Gyakoriság')
    plt.plot()
    plt.show()


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
        for kraj in kraji:
            pattern = re.search(f'.{kraj.casefold()}',str(new_str).casefold())
            if(pattern):
                kraji[f'{kraj}'] += 1

    data_kariera = pd.read_csv(f'../../data/kariera/kariera{initial}.csv')
    location_1  = data_kariera['Location'].to_list()
    remote_works(location_1)
    for lo in location_1:
        new_str = str(lo).replace(',', '')
        for reg in  region.keys():
            pattern = re.search(f'{reg.casefold()}',str(new_str).casefold())
            if(pattern):
                region[f'{reg}'] += 1
            else:
                pass
        for kraj in kraji:
            pattern = re.search(f'{kraj.casefold()}',str(new_str).casefold())
            if(pattern):
                kraji[f'{kraj}'] += 1

    for key , value in region.items():
        if value >20:
            new_region[key] = value
        else:
            pass

for x in range(0,3):
    try:
        main(x)
    except Exception as e:
        raise

barchart()

print('\a')
