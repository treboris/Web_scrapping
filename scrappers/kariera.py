from bs4 import BeautifulSoup
import requests


print("KARIERA.SK-scrapper STARTED")



#https://kariera.zoznam.sk/pracovne-ponuky/informatika-software?od=60


corp = []
main = []
location = []
href = []
salary = []

limit = 0
limit_txt = "?od="

url = (f"https://kariera.zoznam.sk/pracovne-ponuky/informatika-software?{limit_txt}{limit}")
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")

fblock = soup.find('ul' , class_='search-list')
for li in fblock.find_all('li' , class_='clearfix'):
    for div in li.find_all('div' , class_='column2'):
        for h2 in div.find_all('h2'):
            main.append(h2)
            for a in h2.find_all('a'):
                href.append(a.get('href'))
        for emp in div.find_all('a' , class_='employer'):
            corp.append(emp.text)
        for span in div.find_all('span' , class_='place'):
            print(span.text)
            location.append(span.text)
        for span_salary in div.find_all('span' , class_='salary'):
            splitted = span_salary.text.split()
            join = ''.join(splitted[1:3])
            salary.append(join)

print(len(corp))
print(len(main))
print(len(location))
print(len(href))
print(len(salary))
