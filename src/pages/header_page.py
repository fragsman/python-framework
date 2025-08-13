from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.interactor import Interactor
import time

class HeaderPage(BasePage):
    HOME_LINK = (By.XPATH,"//li[@id='menu-item-1226']")
    STORE_LINK = (By.ID,"menu-item-1227")
    CART_ICON = (By.XPATH,"//div[@id='ast-desktop-header']//div[@class='ast-cart-menu-wrap']")
    CART_WIDGET_PROD_NAME = (By.XPATH,"//div[@id='ast-desktop-header']//div[@class='widget_shopping_cart_content']//a[2]")
    CART_WIDGET_CONTENT = (By.XPATH,"//div[@id='ast-desktop-header']//div[@class='widget_shopping_cart_content']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_home_link(self):
        Interactor.find_element(self.driver,self.HOME_LINK).click()

    def click_store_menu(self):
        Interactor.find_element(self.driver,self.STORE_LINK).click()

    def display_cart_menu(self):
        Interactor.hover_to_element(self.driver,self.CART_ICON)
        Interactor.wait_for_element_to_be_visible(self.driver,self.CART_WIDGET_CONTENT)

    def get_first_item_name_in_cart(self) -> str:
        return Interactor.find_element(self.driver,self.CART_WIDGET_PROD_NAME).text