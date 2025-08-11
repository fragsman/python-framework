from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage

class StorePage(BasePage):
    loc_header_text = "header h1"
    loc_search_bar = "woocommerce-product-search-field-0"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_header_text(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR,StorePage.loc_header_text).text
    
    def search_item(self,text: str):
        search_bar = self.driver.find_element(By.ID,StorePage.loc_search_bar)
        search_bar.clear()
        search_bar.send_keys(text)
        search_bar.send_keys(Keys.RETURN)

    def click_product_image(self, product_name: str):
        product_image = self.driver.find_element(By.XPATH,"//h2[contains(text(),'"+product_name+"')]/parent::a")
        product_image.click()
