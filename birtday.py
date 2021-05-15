from selenium import webdriver
import time

driver=webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://web.whatsapp.com/")
print("scan the qr code")
time.sleep(10)


name_of_the_user=driver.find_element_by_xpath('//span[contains(@title,"Shiva Sankar")]')
name_of_the_user.click()

msg_box=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
for i in range(50):
    msg_box.send_keys("test msg")
    send_key=driver.find_element_by_class_name('_1E0Oz')
    send_key.click()
