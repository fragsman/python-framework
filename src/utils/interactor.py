# I import WebDriver to make use of auto-complete. If I need to set up Chrome driver (for example), delete this line
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from src.utils.logger import Logger
import time

class Interactor:

    @staticmethod
    def send_keys(driver: WebDriver, locator: tuple, text: str):
        Logger.debug_msg(f"sending keys to locator: {locator}")
        text_field = Interactor.find_element(driver, locator)
        text_field.clear()
        text_field.send_keys(text)
        text_field.send_keys(Keys.RETURN)

    @staticmethod
    def find_element(driver: WebDriver, locator: tuple) -> WebElement:
        try:
            Logger.debug_msg(f"finding element via locator: {locator}")
            driver.find_element
            element = WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
        except StaleElementReferenceException:
            Logger.error_msg(f"element with locator: {locator} not found")
        return element
    
    @staticmethod
    def hover_to_element(driver: WebDriver, locator: tuple):
        Logger.debug_msg(f"hovering to element via locator: {locator}")
        element = Interactor.find_element(driver,locator)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    @staticmethod
    def wait_for_element_to_be_visible(driver: WebDriver, locator: tuple):
        Logger.debug_msg(f"wait for element to be visible, locator: {locator}")
        WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))