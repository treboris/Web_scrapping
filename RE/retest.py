import re
import os

corpus = {}
txtcorpus = 'selyetanterv'

with open(f'CORPUS/{txtcorpus}.txt' , 'r') as f:
    line = f.read().splitlines()
    for l in line:
        corpus[l.casefold()] = 0

with open(f'data/cvonline/main0.txt') as main:
    lines = main.read().splitlines()
    for line in lines:
        for corp in corpus.keys():
            pattern = re.search(f'.{re.escape(corp)}',line.casefold())
            if (pattern):
                corpus[f'{corp}'] += 1
            else:
                pass
print(corpus)
