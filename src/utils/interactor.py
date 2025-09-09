# I import WebDriver to make use of auto-complete. If I need to set up Chrome driver (for example), delete this line
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from typing import List
import time
from src.utils.logger import Logger

class Interactor:

    SELECT_INPUT_SEARCH_BOX = (By.CSS_SELECTOR,"input.select2-search__field")
    SELECT_RESULTS = (By.CSS_SELECTOR,"span.select2-results ul li")
    OVERLAY_BLOCKERS = (By.CSS_SELECTOR,"div.blockUI.blockOverlay")

    @staticmethod
    def accurate_click(driver: WebDriver, locator:tuple):
        try:
            Logger.debug_msg(f"acurate clicking")
            element = Interactor.find_element(driver,tuple)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable(element))
            element.click()
        except Exception:
            Logger.error_msg(f"failed to click element")

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
            element = WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
        except StaleElementReferenceException:
            Logger.error_msg(f"element with locator: {locator} not found")
        return element
    
    @staticmethod
    def find_elements(driver: WebDriver, locator: tuple) -> List[WebElement]:
        try:
            Logger.debug_msg(f"finding elements via locator: {locator}")
            elements = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(locator))
        except StaleElementReferenceException:
            Logger.error_msg(f"elements with locator: {locator} not found")
        return elements
    
    @staticmethod
    def hover_to_element(driver: WebDriver, locator: tuple):
        Logger.debug_msg(f"hovering to element via locator: {locator}")
        element = Interactor.find_element(driver,locator)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    @staticmethod
    def select_nth_element(element: WebElement, position: int):
        try:
            element.find_elements(*(By.TAG_NAME,"li"))[position].click() #To understand the * go to Learned Lessons in README.md
        except IndexError:
            Logger.error_msg(f"There is no such position: {position}")

    """
    The implementation of this will depend on the website.
    In general all select elements withing a same web-page will be exactly the same. So this should work for an entire web-page.
    """
    @staticmethod
    def select_option(driver: WebDriver,locator: tuple, option: str):
        Interactor.find_element(driver,locator).click() # Opens the selector, ready to receive text
        selector_search_box = Interactor.find_element(driver, Interactor.SELECT_INPUT_SEARCH_BOX) 
        selector_search_box.send_keys(option) # Send text

        resulting_option = Interactor.find_element(driver, Interactor.SELECT_RESULTS)
        resulting_option.click() # Click on the option (there should be one)

    """
    A BlockingOverlays is basically a loading spinner that prevents the web to be used. This element does not always
    appear and is not very clear in which situation it does. As I'm testing on a public-web I can't ask the developer to see when
    this gets triggered. When it does, it is for less than 2 seconds. Thus, it requires a special treatment
    """
    @staticmethod
    def wait_for_blocking_overlays(driver: WebDriver):
        blocking_overlays = []
        try:
            Logger.debug_msg(f"finding blocking overlays")
            blocking_overlays = WebDriverWait(driver,2).until(EC.presence_of_all_elements_located(Interactor.OVERLAY_BLOCKERS))
        except TimeoutException:
            Logger.error_msg(f"failed to find overlays")
        if(len(blocking_overlays) > 0):
            Logger.debug_msg(f"Found {len(blocking_overlays)} overlays, waiting...")
            time.sleep(2) #TODO Java can check for invisibility of-all-elements (blocking_overlays). Not Py. Research.


    @staticmethod
    def wait_for_element_to_be_visible(driver: WebDriver, locator: tuple):
        Logger.debug_msg(f"wait for element to be visible, locator: {locator}")
        WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))