import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

# When you use yield in a fixture function, the set-up code is executed before the first yield, and the tear-down code 
# is executed after the last yield. In general, yield is often used when you need to set up and tear down some 
# resources for each test function

@pytest.fixture(scope="function") 
def driver():
    #This is the set-up
    myOptions = Options()
    #Disable Edge Logs Warnings/Errors which makes output harder to read. If things breaks, comment the following line.
    myOptions.add_experimental_option('excludeSwitches', ['enable-logging']) 
    driver = webdriver.Edge(options=myOptions)
    driver.get("https://askomdch.com")
    driver.maximize_window()
    yield driver
    #This is is the tear-down
    driver.quit()
    driver = None