from selenium import webdriver
from selenium.webdriver.edge.options import Options

class BaseTest:
    driver = None #This is similar to a null in Java

    def __init__(self):
        pass
        
    def setup(self):
        print("setup")
        if not BaseTest.driver: #singleton implementation
            myOptions = Options()
            BaseTest.driver = webdriver.Edge(options=myOptions)
            self.driver = BaseTest.driver

    def close_driver(self):
        if BaseTest.driver:
            BaseTest.driver.quit()
            BaseTest.driver = None

    def navigate(self):
        self.driver.get("https://www.python.org")
