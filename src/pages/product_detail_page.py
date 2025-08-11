from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from src.pages.base_page import BasePage

class ProductDetailPage(BasePage):

    loc_add_to_cart = "//button[contains(text(),'Add to cart')]"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_product_to_cart(self):
        add_to_cart = self.driver.find_element(By.XPATH,ProductDetailPage.loc_add_to_cart)
        add_to_cart.click()