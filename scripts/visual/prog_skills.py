import matplotlib
import pandas as pd
import shutil
import glob
import re
import os
import time

corpustxt = {}
matches = {}
files = []

#FILL CORPUSTXT LIST
def corpus(name):
    with open(f"CORPUS/{name}", 'r') as file:
        line = file.read().splitlines()
        for l in line:
            corpustxt[l.casefold()] = 0

#COUNT JOB TXT FILES
def file_count(path):
    file_count = len(glob.glob1(path,"*.txt"))
    for x in range(0,file_count):
        files.append(f'job{x}.txt')

#LINK FILES
def link_files():
    file_count('txt/0')
    with open('data/cvonline/main0.txt','wb') as main:
        for f in files:
            with open(f'txt/0/{f}','rb') as jobtxt:
                shutil.copyfileobj(jobtxt,main)


def barchart():
    fig, ax = plt.subplots(layout='constrained')
    data = matches
    plt.title("Kulcsszógyakoriság adott szöveghalmazban")
    ax.set_title('Programozási nyelvek')
    ax.bar(*zip(*data.items()), color=['brown' , 'darkolivegreen','steelblue' , 'chocolate'])
    ax.set_ylim(0, 1500)
    ax.set_ylabel('Gyakoriság')
    plt.show()


#REGEX
def keyword_search(limit):
    corpus('sulibantanultak.txt')
    if os.stat(f'data/cvonline/main{limit}.txt').st_size == 0:
        link_files()
    else:
        pass

    with open(f'data/cvonline/main{limit}.txt') as main:
        lines = main.read().splitlines()
        for line in lines:
            #time.sleep(1)
            for corp in corpustxt.keys():

                pattern = re.search(f'.{re.escape(corp)}',line.casefold())
                if (pattern):
                    corpustxt[f'{corp}'] += 1
                else:
                    pass

    for match in corpustxt.keys():
        if(corpustxt.get(match) > 0):
            matches[f'{match}'] = corpustxt.get(match)


keyword_search('0')

print(f'Talalatok: {matches}')
