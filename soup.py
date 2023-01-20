from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


from bs4 import BeautifulSoup
import requests


url = (f"https://www.profession.hu/allasok/budapest/1,10_25,23,0,69_70_72_73_75_76_77_78_79_80_200_201_202_338_363_365_393")



def conn(page):
    url = (f"https://www.profession.hu/allasok/budapest/{page},10_25,23,0,69_70_72_73_75_76_77_78_79_80_200_201_202_338_363_365_393")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    return soup



def save_html(soup):
    try:
        with open("profession.hu", "w") as file:
            file.write(str(soup))
            print("Ok")
    except:
        print("An error has occurred.")



#save_html((conn(1).prettify()))

#SEARCH RESULTS
search_results = conn(1).find(id="jobs_block_count")
search_results_numbers = search_results.text.split()
print(f"Talalatok: {search_results_numbers[0]}")

#TITLES
browser = webdriver.Firefox()
url = "https://www.profession.hu/"
browser.get(url)
title_1 = browser.find_element(By.XPATH,"//*[@id='jobs_headline2_title_highlight-2022138']/a")
print(title_1.getText)


browser.close()








titles = conn(1).find_all("a",class_="job-card__title ga-enchanced-event-click")
if titles:
    for tit in titles:
        print(tit.text.strip())
else:
    print("Not found titles.")
#print(f"Title: {titles.text.strip()}")





#ORGANIZATION
org = conn(1).find("a" , class_="link-icon")
print(f"Org: {org.text.strip()}")
#TAGS





#UPLOAD-DATE
upload_date = conn(1).find("div",class_="job-card__date date")
print(f"Upload date: {upload_date.text.split()}")



# all_list = soup.find_all(name = "a")
#
#
# for tag in all_list:
#     print(tag.getText())
#     print("--------------------")
#     print(tag.get("href"))
# print(all_list)
#
#
# print("**********************")
# heading = soup.find(name = "h3", class_= "heading")
# print(heading.get("class"))
