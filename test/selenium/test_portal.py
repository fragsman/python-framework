from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from base_test import BaseTest
import pytest

class TestPortal(BaseTest):

    @pytest.mark.skip(reason="Testing")
    def test_store_link_leads_to_store_page(self):
        self.setup()
        self.navigate()
        link_store = self.driver.find_element(By.ID,"menu-item-1227")
        link_store.click()
        header_text = self.driver.find_element(By.CSS_SELECTOR,"header h1").text
        assert header_text == "Store"
        self.close_driver()

    @pytest.mark.skip(reason="Testing")
    def test_store_link_url(self):
        self.setup()
        self.navigate()
        link_store = self.driver.find_element(By.ID,"menu-item-1227")
        link_store.click()
        assert self.driver.current_url == "https://askomdch.com/store/"
        self.close_driver()

    @pytest.mark.skip(reason="Testing")
    def test_search_bar_in_store(self):
        self.setup()
        self.navigate()
        link_store = self.driver.find_element(By.ID,"menu-item-1227")
        link_store.click()
        search_bar = self.driver.find_element(By.ID,"woocommerce-product-search-field-0")
        search_bar.clear()
        search_bar.send_keys("shoes")
        search_bar.send_keys(Keys.RETURN)
        search_results_header = self.driver.find_element(By.CSS_SELECTOR,"header h1").text
        assert search_results_header == "Search results: “shoes”"
        self.close_driver()

    
    @pytest.mark.skip(reason="Testing")
    def test_ignored_test():
        assert "a" == "b"
