from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

score = 0

username = input("Username: ")
password = input("password: ")
#SELENIUM HEADLESS MODE
# options = Options()
# options.headless = True

url = "https://ncore.pro/login.php"
browser = webdriver.Firefox()
browser.get(url)

def save_html(soup):
    try:
        with open("ncore.html", "w") as file:
            file.write(str(soup))
            print("Ok")
    except:
        print("An error has occurred.")

def login(username , password):
    nevmezo = browser.find_element(By.XPATH,"//*[@id='nev']")
    nevmezo.click()
    nevmezo.send_keys(username)
    time.sleep(1)
    passw = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/form/table/tbody/tr[2]/td[2]/input")
    passw.click()
    passw.send_keys(password)
    time.sleep(1)
    if (passw):
        button = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/form/table/tbody/tr[1]/td[3]/input")
        button.click()
    #LOGIN DELAY
    print("Logged")
    time.sleep(1)
    button_letoltes = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div[4]").click()


#DELAY HOGY BETOLTODJON
time.sleep(2)

#LOGIN
login(username,password)

while (True):
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,"html.parser")
    spooky = soup.find("div",id="spo0kyD")
    if(spooky):
        try:
            browser.find_element(By.ID,"spo0kyD").click()
            print("Talalt fogott...")
            score+=1
        except Exception as e:
            raise Exception(e)
    else:
        pass
