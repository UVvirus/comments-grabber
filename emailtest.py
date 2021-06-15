from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time
import re
import tldextract
import socket
import smtplib
import dns
import dns.resolver
from Check_Valid_Email import Main


# ext=tldextract.extract("https://acviss")
# print("0",ext[0])
# print("1",ext[1])
# print(ext[2])

search_term = input("Enter the domain name in this format[domain.com]:-")
ext=tldextract.extract(search_term)
url = f"https://www.linkedin.com/search/results/people/?keywords={ext[1]}&origin=GLOBAL_SEARCH_HEADER"
login_url = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in"

# if you want to run linkedin on background then this option will be helpful
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options, executable_path=r"/usr/local/bin/chromedriver")
# print("headless")

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get(login_url)
time.sleep(5)
# logging in using username and password
emailid=input("Enter the email:")
password=input("Enter the password:")
driver.find_element_by_id("username").send_keys(emailid)
driver.find_element_by_id("password").send_keys(password)

# finding login button and click
driver.find_element_by_class_name("login__form_action_container ").click()
print("Logged in...")

# getting the url of the search
driver.get(url)

empty_list = []
converted_list = []


def locate():
    # This will find all the employees names
    names = driver.find_elements_by_xpath('//span[@aria-hidden="true"]')

    for name in names:

        # This is for checking the blank spaces
        if not isBlank(name.text):
            empty_list.append(name.text)
    print(empty_list)

    # Scroll down to the page end
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4));")
    time.sleep(5)

    element = driver.find_element_by_xpath('//button[@aria-label="Next"]')
    if element.is_enabled() is True:

        # clicking the next button
        driver.execute_script("arguments[0].click();", element)
        locate()
    else:
        email_format(empty_list)


def isBlank(myString):
    if myString and myString.strip():
        # myString is not None AND myString is not empty or blank

        return False

    return True


def email_format(empty_list):
    global firstname
    # converting the capital letters into small letters
    for caps in empty_list:
        small_letter = caps.lower()
        converted_list.append(small_letter)

    for i in converted_list:
        try:
            # regular expresion for space is "\s"
            regex = re.split("\s", i)

            firstname = regex[0]
            lastname = regex[1]

            lastemail=lastname+'@'+ext[1]+"."+ext[2]
            firstlast = firstname + lastname + "@" + ext[1] + "." + ext[2]
            firstnamemail = firstname + "@" + ext[1] + "." + ext[2]
            first_last_mail = firstname + "." + lastname + "@" + ext[1] + "." + ext[2]

            #print(lastemail)
            if Main.valid_email(lastemail)==True:
                print("valid email:", lastemail)
                print("====================================================================================")

            elif Main.valid_email(firstlast)==True:
                print("valid email:", firstlast)
                print("====================================================================================")

            elif Main.valid_email(firstnamemail)==True:
                print("valid email:", firstnamemail)
                print("====================================================================================")

            elif Main.valid_email(first_last_mail) == True:
                print("valid email:", first_last_mail)
                print("====================================================================================")

        # Index error occurs when there is no lastname(regex[1])  Except will handle that exception
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    locate()
