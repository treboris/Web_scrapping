from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

#profession fooldalarol a ket rublikan keresztuli kereses


#options = Options()
#options.headless = True







browser = webdriver.Firefox()
url = "https://www.profession.hu/"
browser.get(url)

time.sleep(2)

#COOKIE ACCEPT
elfogad = browser.find_element(By.ID,"elfogad")
elfogad.click()
time.sleep(2)



print("Elso Oldal\n")
soup  = BeautifulSoup(browser.page_source, "html.parser")




time.sleep(1)
search_location = browser.find_element(By.ID,"header_location")
search_location.click()
search_location.send_keys("Budapest")
search_location.send_keys(Keys.TAB)
time.sleep(1)

search = browser.find_element(By.ID,"header_keyword")
search.click()
search.send_keys("Programozó")

search_button = browser.find_element(By.ID,"search-bar-search-button")
search_button.click()

# title = soup.find('title')
# print(title.string)


# element = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[3]/a")
# element.click()
#
# time.sleep(2)
# element = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[3]/a")
# element.click()
#
# time.sleep(2)
# element = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[3]/a")
# element.click()
#
# time.sleep(2)
# element = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[3]/a")
# element.click()




print("Masodik oldal")
title = soup.find('title')


#browser.quit()


#search_by_class = browser.find_elements(By.CLASS_NAME,"link-icon")
