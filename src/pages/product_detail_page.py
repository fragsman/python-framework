from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.interactor import Interactor

class ProductDetailPage(BasePage):

    ADD_TO_CART = (By.XPATH,"//button[contains(text(),'Add to cart')]")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self):
        Interactor.find_element(self.driver,self.ADD_TO_CART).click()