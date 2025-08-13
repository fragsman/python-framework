from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.interactor import Interactor

class StorePage(BasePage):
    HEADER_TEXT = (By.CSS_SELECTOR,"header h1")
    SEARCH_BAR = (By.ID,"woocommerce-product-search-field-0")
    PRODUCT_NAME = ""
    PRODUCT_IMAGE = (By.XPATH,f"//h2[contains(text(),'{PRODUCT_NAME}')]/parent::a")

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self) -> str:
        return Interactor.find_element(self.driver,self.HEADER_TEXT).text
    
    def search_item(self,text: str):
        Interactor.send_keys(self.driver,self.SEARCH_BAR,text)

    def click_product_image(self, product_name: str):
        self.PRODUCT_NAME = product_name
        Interactor.find_element(self.driver,self.PRODUCT_IMAGE).click()
