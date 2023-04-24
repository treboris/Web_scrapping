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

df = pd.DataFrame(list(matches.items()), columns=['rank', 'count'])
df.to_csv('diagram_data/piechart.csv', index=False)
print('\a')
