from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
import requests




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://seniorautomationtest.com/")

time.sleep(3)

service_button = self.driver.find_element_by_xpath('//a[@href="/services/"]')
service_button.click()

time.sleep(3)
self.assertEqual(//span[@class ='text-capitalize small font-weight-bold'].text, "DỊCH VỤ")

driver.quit()

