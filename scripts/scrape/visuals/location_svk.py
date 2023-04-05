import plotly.express as px
import pandas as pd
import re


graph_data = pd.read_csv('test.csv')
import seaborn as sns

df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")

graph_data = pd.read_csv('test.csv')
# Here we use a column with categorical data
fig = px.histogram(graph_data, x="loc")
fig.show()

data = pd.read_csv('../data/kariera0.csv')
locations = data['Location'].to_list()

def remote_works():
    main = data['Main'].to_list()
    count = 0
    words = ['[remote]' ,'[Remote]','[REMOTE]', '[práca z domu]','[Práca z domu]' ]
    for m in main:
        for x in range(0,len(words)):
            result = re.match(words[x] , m)
            if(result):
                count +=1

    return count

#print(f'Remote works: {remote_count()}')

def filter(list):
    filtered = [*set(list)]
    for f in filtered:
        #print(f)
        pass
    return filtered

def counter(list):
    for l in list:
        count = locations.count(f'{l}')
        print(f'{l}: {count} ')





filtered_locations = filter(locations)
counter(filtered_locations)
