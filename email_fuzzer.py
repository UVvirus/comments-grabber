from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.linkedin.com/search/results/people/?keywords=isteer&origin=GLOBAL_SEARCH_HEADER"
login_url = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in"


#Below 4 lines can be used for headless browser
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options, executable_path=r"/usr/local/bin/chromedriver")
# print("headless")

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get(login_url)

driver.find_element_by_id("username").send_keys("yuvasyuvarajan@gmail.com")
driver.find_element_by_id("password").send_keys("P@$$w0rd")
driver.find_element_by_class_name("login__form_action_container ").click()
print("Logged in...")
driver.get(url)


def locate():
    names = driver.find_elements_by_xpath('//span[@aria-hidden="true"]')
    with open("names.json","w")as file:
        for name in names:
            if not isBlank(name.text):
                print(name.text)
            file.writelines(name.text)


    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4));")
    time.sleep(5)
    element = driver.find_element_by_xpath('//button[@aria-label="Next"]')
    driver.execute_script("arguments[0].click();", element)

    time.sleep(5)


def isBlank(myString):
    if myString and myString.strip():
        # myString is not None AND myString is not empty or blank

        return False

    return True

"""
def email_format():
    firstname=[]
    lastname=[]
    regex='^[a-z0-9]+[@]\w+[.]{2,3}$'
    if " " in "names.txt":
        lastname.append()
    else:
        firstname.append()
"""
if __name__ == "__main__":
    while True:
        locate()
