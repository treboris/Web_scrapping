import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

bratislava = 0
zilina = 0
kosice = 0
remote = 0
betuk =["Bratislava","Žilina","Košice" , "Remote work","Práce z domu"]



data_frame = pd.read_csv("data/Professia.csv")
location = data_frame[["Location"]]
for loc in location.values:
    x = "".join(loc)
    print(x)
    m = re.compile(f'^[{betuk[0]}]+$')
    if (m.match(x)):
        bratislava += 1
    m = re.compile(f'^[{betuk[1]}]+$')
    if (m.match(x)):
        zilina += 1

    m = re.compile(f'^[{betuk[2]}]+$')
    if (m.match(x)):
        kosice += 1

    m = re.compile(f'^[{betuk[3]}]+$')
    if (m.match(x)):
        remote += 1

    m = re.compile(f'^[{betuk[4]}]+$')
    if (m.match(x)):
        remote += 1

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['Bratislava', 'Žilina', 'Košice', 'Remote work']
counts = [bratislava, zilina, kosice, remote]
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:red']

ax.bar(fruits, counts, color=bar_colors)

ax.set_ylabel('COUNTS')
ax.set_title('FELADOTT HIRDETESEK BIZONYOS TELEPULESEKEN')

plt.show()
