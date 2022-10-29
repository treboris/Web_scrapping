from bs4 import BeautifulSoup
import requests
import re




conn = requests.get("https://www.profession.hu/allasok/1,0,0,programoz%c3%b3%401%401?keywordsearch")

ycom_web_page = conn.text






soup = BeautifulSoup(ycom_web_page,"html.parser")
pretty = soup.prettify()

#Copy webpage
try:
    with open("mentes.html", "w") as file:
        file.write(str(pretty))
        print("||OK||")
except:
    print("Nem irta ki.")
