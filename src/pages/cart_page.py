from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.interactor import Interactor

class CartPage(BasePage):

    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR,"div.wc-proceed-to-checkout > a")

    def __init__(self, driver):
        super().__init__(driver)

    def proceed_to_checkout(self):
        Interactor.find_element(self.driver, self.PROCEED_TO_CHECKOUT).click()