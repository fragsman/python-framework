from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.service import Service
import os

def greet():
    print("Hello world")

def testOne():
    myOptions = Options()
    driver = webdriver.Edge(options=myOptions)
    driver.get("https://www.python.org")
    print(driver.title)
    search_bar = driver.find_element(By.NAME,"q")
    search_bar.clear()
    search_bar.send_keys("getting started with python")
    search_bar.send_keys(Keys.RETURN)
    print(driver.current_url)
    driver.close()

greet()
testOne()