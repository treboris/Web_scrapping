import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import pandas as pd
import re



web_pages= ['cvonline' , 'itpeople','jobline', 'profession']
region = {'Budapest' : 0,'Debrecen' : 0,'Szeged' : 0 ,'Miskolc' : 0 ,
            'Pécs' : 0 ,'Győr' : 0 , 'Kecskemét' : 0 , 'Székesfehérvár' : 0 ,
            'Szombathely' : 0 ,'Remote' : 0
            }


def add_labels():
    labels = []
    for x in region.values():
        labels.append(x)
    for i in range(len(labels)):
        plt.text(i, labels[i], labels[i], ha = 'center')

def barchart():
    fig, ax = plt.subplots(layout='constrained')
    add_labels()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    data = region
    plt.title("Feladott hirdetések települések szerint")
    ax.set_title('Települések')
    ax.bar(*zip(*data.items()), color=['brown' , 'darkolivegreen','steelblue' , 'chocolate'])
    ax.set_ylim(0, 5500)
    ax.set_ylabel('Gyakoriság')
    plt.show()


def remote_works(list):
    words = ['remote' , 'otthonról']
    for l in list:
        for w in words:
            pattern = re.search(f'{w.casefold()}',str(l).casefold())
            if(pattern):
                region['Remote'] +=1

def main(webpage,initial):
    data_professia = pd.read_csv(f'../../data/{webpage}/{webpage}{initial}.csv')
    location = data_professia['Location'].to_list()
    remote_works(location)
    for l in location:
        new_str = str(l).replace(',', '')
        for reg in region.keys():
            pattern = re.search(f'{reg.casefold()}',new_str.casefold())
            if(pattern):
                region[f'{reg}'] += 1


for x in range(len(web_pages)):
    for y in range(0,3):
        main(web_pages[x],y)


df = pd.DataFrame(list(region.items()), columns=['city', 'count'])
df.to_csv('diagram_data/location_hun.csv', index=False)
print('\a')
