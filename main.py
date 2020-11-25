from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup,Comment
import argparse

def page_source():
    try:
        url=input('Enter the site:')
        driver=webdriver.Chrome("/usr/local/bin/chromedriver")
        #url="http://scanme.nmap.org"
        driver.get(url)
        soup=BeautifulSoup(driver.page_source,'html.parser')

        driver.quit()
        for comments in soup.findAll(text=lambda text: isinstance(text, Comment)):
            """""
            The condition in our case is,

            3.1.Firstly
            we
            don't check everything only the clear, plain English text and inside tags, and/or 
            whatever string there is. That's text =

            3.2.The text also hasa condition, it doesn't take any text, 
            only if a lambda function returns True, 
            i.e. fulfills the condition of the lambda.

            3.3.The lambda condition is that it has to be an instance 
            of Comment meaning only if it's a Comment it will return True.
            """""
            comments.extract()
            print(comments)
    except NoSuchElementException as e:
        print(e)

#page_source()

if __name__ == '__main__':
        parser=argparse.ArgumentParser(usage="python3 c.py http://siteName.com",
        description="Description:This program grabs comments from "
                    "source code of a website")
        args=parser.parse_args()
        #parser.add_argument('-c','comment',)
        page_source()