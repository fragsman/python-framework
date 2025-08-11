from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from src.pages.base_page import BasePage
import time

class HeaderPage(BasePage):
    loc_home_link = "//li[@id='menu-item-1226']"
    loc_store_link = "menu-item-1227"
    loc_cart_icon = "//div[@id='ast-desktop-header']//div[@class='ast-cart-menu-wrap']"
    loc_cart_menu_product_name = "//div[@id='ast-desktop-header']//div[@class='widget_shopping_cart_content']//a[2]"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_home_link(self):
        self.driver.find_element(By.ID,HeaderPage.loc_home_link)

    def click_store_menu(self):
        self.driver.find_element(By.ID,HeaderPage.loc_store_link).click()

    def display_cart_menu(self):
        cart_icon = self.driver.find_element(By.XPATH, HeaderPage.loc_cart_icon)
        actions = ActionChains(self.driver)
        actions.move_to_element(cart_icon).perform()
        time.sleep(1) #replace with explicit wait until cart window is visible

    def get_first_item_name_in_cart(self) -> str:
        return self.driver.find_element(By.XPATH,HeaderPage.loc_cart_menu_product_name).text