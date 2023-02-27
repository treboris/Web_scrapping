from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


#legkozelebb ezzel  kezdem asdadasdasd
# https://stackoverflow.com/questions/27112731/selenium-common-exceptions-nosuchelementexception-message-unable-to-locate-ele


browser = webdriver.Firefox()
url = "https://www.profession.hu/allasok/1,10_25,0,programoz%c3%b3%401%401,69_70_72_73_75_76_77_78_79_80_200_201_202_338_363_365_393?keywordsearch"
browser.get(url)
time.sleep(1)

#BF4
soup  = BeautifulSoup(browser.page_source, "html.parser")





#COOKIE ACCEPT
elfogad = browser.find_element(By.ID,"elfogad")
elfogad.click()
time.sleep(1)


gomb = browser.find_element(By.XPATH,'//*[@id="jobs_headline2_title_highlight-2016804"]')
gomb.click()
time.sleep(1)




#ELSO TALALAT
#element = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/div[1]/div/div/div[1]/ul/li[1]/div[1]/div[1]/div[2]/div/h2/a")))

# time.sleep(3)
# # element.click()
# time.sleep(1)
# if (element):
#     print("Talalt")
#     print(element)
# else:
#     print("Nemtalalt")





time.sleep(3)
# browser.quit()
