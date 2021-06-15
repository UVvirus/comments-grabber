from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import json
import re
from user_agents import Core
import requests
#
# search_term = "isteer"
# url = f"https://www.linkedin.com/search/results/people/?keywords={search_term}&origin=GLOBAL_SEARCH_HEADER"
# login_url = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in"
#
# # if you want to run linkedin on background then this option will be helpful
# # options = Options()
# # options.headless = True
# # driver = webdriver.Chrome(options=options, executable_path=r"/usr/local/bin/chromedriver")
# # print("headless")
#
# driver = webdriver.Chrome("/usr/local/bin/chromedriver")
#
# driver.get(login_url)
#
# driver.find_element_by_id("username").send_keys("test@gmail.com")
# driver.find_element_by_id("password").send_keys("password")
#
# # finding login button and click
# driver.find_element_by_class_name("login__form_action_container ").click()
# print("Logged in...")
#
# # getting the url of the search
# driver.get(url)
#
# empty_list = []
# converted_list = []


# def locate():
#     # This will find all the employees names
#     names = driver.find_elements_by_xpath('//span[@aria-hidden="true"]')
#
#     for name in names:
#
#         # This is for checking the blank spaces
#         if not isBlank(name.text):
#             empty_list.append(name.text)
#
#     # Scroll down to the page end
#     driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
#     time.sleep(5)
#     driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4));")
#     time.sleep(5)
#
#     # finding the "Next" button
#     element = driver.find_element_by_xpath('//button[@aria-label="Next"]')
#     # clicking the next button
#     driver.execute_script("arguments[0].click();", element)
#     # 5 secs for page to load
#     time.sleep(5)
#
#     # time.sleep(5)
#
#
# def isBlank(myString):
#     if myString and myString.strip():
#         # myString is not None AND myString is not empty or blank
#
#         return False
#
#     return True
#
#
# def email_format(empty_list):
#     global firstname
#     # converting the capital letters into small letters
#     for caps in empty_list:
#         small_letter = caps.lower()
#         converted_list.append(small_letter)
#
#     for i in converted_list:
#         try:
#             # regular expresion for space is "\s"
#             regex = re.split("\s", i)
#
#             firstname = regex[0]
#             lastname = regex[1]
#
#             first_last_mail = firstname + "." + lastname + "@" + search_term + ".com"
#
#             is_it_a_real_email_api(first_last_mail)
#             print("====================================================================================")
#         # Index error occurs when there is no lastname(regex[1])  Except will handle that exception
#         except IndexError:
#             firstnamemail = firstname + "@" + search_term + ".com"
#
#             is_it_a_real_email_api(firstnamemail)
#             print("====================================================================================")
#
#
# def is_it_a_real_email_api(email):
#     url = f"https://isitarealemail.com/api/email/validate?email={email}"
#     agent = Core.get_user_agent()
#     header = {'User-Agent': agent}
#
#     res = requests.get(url, headers=header)
#     print(res.text)
#
#
# """
#
# for i in range(len(empty_list)):
#     valid_mail_number = 0
#     if "valid" in res.text:
#         valid_mail_number += 1
#         if valid_mail_number >= 3:
#             format(email)
# """
#
#
# def format(that_format):
#     url = f"https://isitarealemail.com/api/email/validate?email={that_format}"
#     agent = Core.get_user_agent()
#     header = {'User-Agent': agent}
#
#     res = requests.get(url, headers=header)
#     if "valid" in res.text:
#         print(res.text)
#         print("formaat function")

def test():
    code = 250
    if code == 250:
        print("hello")
        return True
    else:
        return False
if __name__ == "__main__":
    if test() == True:
        print("valid")
    # while True:
    #     locate()
    # email_format(empty_list)

""""
    for i in range(0,2):
        locate()
    email_format(empty_list)


    i = 1
    try:
        #lastpage=driver.find_element_by_xpath('//button[@aria-label="Page 26"]')
        end_page = driver.find_element_by_xpath('//button[@disabled=""]')
        email_format(empty_list)
    except:
        while True:
            locate()
            i += 1
            print("i value:",i)
"""



