import pandas as pd
import re
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

df = pd.DataFrame(list(keyword_counts.items()), columns=['languages', 'count'])
df.to_csv('diagram_data/programing.csv', index=False)
