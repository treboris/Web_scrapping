from collections import Counter
import pandas as pd

with open('../../data/full_main/full_main.txt', 'r') as f:
    text = f.read().casefold()

df_hun = pd.read_csv('diagram_data/words.csv')

comma = ['support,','time,','office,','véleményét,','programátor,','állásértesítőnket,','kérjük,','állásértesítőnket,','munkaidő,','it,','budapest,','programozó,','kérjük']
excluded_words = df_hun['words'].to_list()
excluded_words.extend(comma)

words = text.split()

word_counts = Counter(word for word in words if word not in excluded_words)
dict_counts ={}

for word, count in word_counts.most_common(20):
    dict_counts[word] = count
    print(f'{word} {count}')

df = pd.DataFrame.from_dict(dict_counts, orient='index', columns=['Count'])
df.to_csv('diagram_data/top200.csv', sep=',', index_label='Word')
