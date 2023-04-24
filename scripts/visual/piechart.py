import matplotlib.pyplot as plt
import pandas as pd
import re
import sys


keywordtxt = {}
matches = {}
try:
    arg_kw = sys.argv[1]
except(IndexError):
    arg_kw = 'piechart'


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
    fig ,ax = plt.subplots()
    data = {k.capitalize(): v for k, v in matches.items()}
    wedges, labels, _ = ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    labels = [f"{label}: {value}" for label, value in data.items()]
    ax.legend(wedges, labels, loc="center right", bbox_to_anchor=(1.2, 0.5),fontsize = 15)
    fig.set_size_inches(8, 6)
    plt.tight_layout()
    plt.show()
#REGEX
def keyword_search():
    keyword(f'{arg_kw}.txt')
    with open(f'../../data/full_main/full_main.txt') as main:
        lines = main.read().splitlines()
        for line in lines:
            #time.sleep(1)
            for corp in keywordtxt.keys():
                pattern = re.search(fr'.\b{re.escape(corp)}\b',line.casefold())
                if (pattern):
                    keywordtxt[f'{corp}'] += 1
                else:
                    pass

    for match in keywordtxt.keys():
        if(keywordtxt.get(match) > 0):
            matches[f'{match}'] = keywordtxt.get(match)

keyword_search()
barchart()
