from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.interactor import Interactor

class CheckoutResults(BasePage):

    CHECKOUT_NOTICE = (By.CSS_SELECTOR,"p.woocommerce-notice")

    def __init__(self, driver):
        super().__init__(driver)

    def get_checkout_notice(self):
        return Interactor.find_element(self.driver,self.CHECKOUT_NOTICE).text