from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from base_test import BaseTest

class PortalTests(BaseTest):

    #This test will try to use hierarchy
    def testOne(self):
        self.setup()
        self.navigate()
        print(self.driver.title)
        search_bar = self.driver.find_element(By.NAME,"q")
        search_bar.clear()
        search_bar.send_keys("getting started with python")
        search_bar.send_keys(Keys.RETURN)
        print(self.driver.current_url)
        self.close_driver()

    def verifySearch(self):
        self.setup()
        self.navigate()
        search_bar = self.driver.find_element(By.NAME,"q")
        search_bar.clear()
        search_bar.send_keys("Frequently asked questions")
        search_bar.send_keys(Keys.RETURN)
        results = self.driver.find_elements(By.XPATH,"//ul[@class='list-recent-events menu']//a")
        #must be 'Python For Beginners'
        print(results[0].text)
        self.close_driver()