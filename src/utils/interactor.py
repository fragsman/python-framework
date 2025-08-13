# I import WebDriver to make use of auto-complete. If I need to set up Chrome driver (for example), delete this line
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time

class Interactor:

    @staticmethod
    def send_keys(driver: WebDriver, locator: tuple, text: str):
        text_field = Interactor.find_element(driver, locator)
        text_field.clear()
        text_field.send_keys(text)
        text_field.send_keys(Keys.RETURN)

    @staticmethod
    def find_element(driver: WebDriver, locator: tuple) -> WebElement:
        try:
            driver.find_element
            element = WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
        except StaleElementReferenceException:
            print("Elemento no encontrado") #replace with a logger
        return element
    
    @staticmethod
    def hover_to_element(driver: WebDriver, locator: tuple):
        element = Interactor.find_element(driver,locator)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    @staticmethod
    def wait_for_element_to_be_visible(driver: WebDriver, locator: tuple):
        WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))