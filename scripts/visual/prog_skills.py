import matplotlib.pyplot as plt
import pandas as pd
import shutil
import glob
import re
import os
import sys

keywordtxt = {}
matches = {}
try:
    arg_kw = sys.argv[1]
except(IndexError):
    arg_kw = 'selyetanterv'


#FILL keywords LIST
def keyword(name):
    with open(f"keywords/{name}", 'r') as file:
        line = file.read().splitlines()
        for l in line:
            keywordtxt[l.casefold()] = 0

def add_labels():
    global max_value
    labels = []
    for x in matches.values():
        labels.append(x)
    for i in range(len(labels)):
        plt.text(i, labels[i], labels[i], ha = 'center')
    max_value = max(matches,key=matches.get)


def barchart():
    fig, ax = plt.subplots(layout='constrained')
    add_labels()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    data = matches
    plt.title("Kulcsszógyakoriság adott szöveghalmazban")
    ax.set_title('Programozási nyelvek es egyebek basszod')
    ax.bar(*zip(*data.items()), color=['brown' , 'darkolivegreen','steelblue' , 'chocolate'])
    ax.set_ylim(0,matches[max_value]+1000)
    ax.set_ylabel('Gyakoriság')
    plt.show()

#REGEX
def keyword_search():
    keyword(f'{arg_kw}.txt')
    with open(f'../../data/full_main/full_main.txt') as main:
        lines = main.read().splitlines()
        for line in lines:
            #time.sleep(1)
            for corp in keywordtxt.keys():

                pattern = re.search(f'.{re.escape(corp)}',line.casefold())
                if (pattern):
                    keywordtxt[f'{corp}'] += 1
                else:
                    pass

    for match in keywordtxt.keys():
        if(keywordtxt.get(match) > 0):
            matches[f'{match}'] = keywordtxt.get(match)

keyword_search()
barchart()
