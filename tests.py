from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
import requests


from helium.api import *

set_driver(driver)
click(Point(123, 456))



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://maticstaker.io/?ref=0x324d8b6df22c6cacb49a63d4772397530d7df622&fbclid=IwAR3Gvd2_BZQAYlHNjh2a4qPs3ji_F9o4eyW6Z5tbMaoaKY6RdKanp-C2XYk")



time.sleep(2)
count = 0
while (count < 10):
    Total_Contract = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/span/span").text

    if Total_Contract == '0.00 MATIC':
        count += 1 
        time.sleep(count)
    elif Total_Contract != '0.00 MATIC':
        print(Total_Contract)
        mouse.move("547", "508")
        mouse.click()
        time.sleep(2)
        
        break



driver.quit()

