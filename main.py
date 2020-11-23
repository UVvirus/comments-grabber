from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup,Comment
"""""
browser=webdriver.Chrome("/usr/local/bin/chromedriver")

#browser.maximize_window()
browser.get("http://scanme.nmap.org/")
tst=browser.find_element(By.TAG_NAME("head")).send_keys(Keys.F12)

"""""

def page_source():
    try:
        driver=webdriver.Chrome("/usr/local/bin/chromedriver")
       # url="scanme.nmap.org"
        driver.get("http://scanme.nmap.org")
        soup=BeautifulSoup(driver.page_source,'html.parser')
        #soup.find_all("<a>")
        driver.quit()
        for comments in soup.findAll(text=lambda text: isinstance(text, Comment)):
            comments.extract()
            print(comments)
    except NoSuchElementException as e:
        print(e)

page_source()