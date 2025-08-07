from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base_test import BaseTest
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestPortal(BaseTest):

    def test_store_link_leads_to_store_page(self,driver):
        super().navigate(driver)
        link_store = driver.find_element(By.ID,"menu-item-1227")
        link_store.click()
        header_text = driver.find_element(By.CSS_SELECTOR,"header h1").text
        assert header_text == "Store"

    def test_store_link_url(self,driver):
        super().navigate(driver)
        link_store = driver.find_element(By.ID,"menu-item-1227")
        link_store.click()
        assert driver.current_url == "https://askomdch.com/store/"

    def test_search_bar_in_store(self,driver):
        super().navigate(driver)
        link_store = driver.find_element(By.ID,"menu-item-1227")
        link_store.click()
        search_bar = driver.find_element(By.ID,"woocommerce-product-search-field-0")
        search_bar.clear()
        search_bar.send_keys("shoes")
        search_bar.send_keys(Keys.RETURN)
        search_results_header = driver.find_element(By.CSS_SELECTOR,"header h1").text
        assert search_results_header == "Search results: “shoes”"

    def test_add_product_to_cart(self,driver):
        super().navigate(driver)
        product = "Anchor Bracelet"
        link_store = driver.find_element(By.ID,"menu-item-1227")
        link_store.click()
        product_image = driver.find_element(By.XPATH,"//h2[contains(text(),'"+product+"')]/parent::a")
        product_image.click()
        add_to_cart = driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]")
        add_to_cart.click()
        cart_icon = driver.find_element(By.XPATH, "//div[@id='ast-desktop-header']//div[@class='ast-cart-menu-wrap']")
        actions = ActionChains(driver)
        actions.move_to_element(cart_icon).perform()
        time.sleep(1) #replace with explicit wait until cart window is visible
        cart_item = driver.find_element(By.XPATH,"//div[@id='ast-desktop-header']//div[@class='widget_shopping_cart_content']//a[2]").text
        assert cart_item == product

    @pytest.mark.skip(reason="Testing")
    def test_ignored_test():
        assert "a" == "b"
