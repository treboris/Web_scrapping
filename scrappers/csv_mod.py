import pandas
import re





data = pandas.read_csv('test.csv')
data_dict = data.to_dict()
main = data['Main'].to_list()
corp = data['Corporation'].to_list()

b = 0

for c in corp:
    if(c == 'Thyssenkrupp'):
        b+=1


print('Corporations is : ' + corp[0]+ " " + "\nMain is: " + main[0])
print(b)
