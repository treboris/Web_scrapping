import matplotlib.pyplot as plt
import re
import os
import sys

keywordtxt = {}

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
    for x in keyword_counts.values():
        labels.append(x)
    for i in range(len(labels)):
        plt.text(i, labels[i], labels[i], ha = 'center')
    max_value = max(keyword_counts,key=keyword_counts.get)

def barchart():
    fig, ax = plt.subplots(layout='constrained')
    add_labels()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    data = keyword_counts
    plt.title("Kulcsszógyakoriság adott szöveghalmazban")
    ax.set_title('Programozási nyelvek es egyebek basszod')
    ax.bar(*zip(*data.items()), color=['brown' , 'darkolivegreen','steelblue' , 'chocolate'])
    ax.set_ylim(0,data[max_value]+1000)
    ax.set_ylabel('Gyakoriság')
    plt.show()

#REGEX
def keyword_search():
    global keywordtxt
    keyword(f'{arg_kw}.txt')
    global keyword_counts
    keyword_counts = keywordtxt.copy()
    with open(f'../../data/full_main/full_main.txt') as main:
        lines = main.read().splitlines()
        for line in lines:
            for corp in keywordtxt.keys():
                pattern = re.compile(fr'(?<!\w){re.escape(corp)}(?!\w)')
                matches = pattern.findall(line.casefold())
                if matches:
                    keyword_counts[f'{corp}'] += len(matches)
    print(keyword_counts)

keyword_search()
barchart()
