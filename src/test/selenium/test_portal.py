import pytest
from selenium.webdriver.common.by import By
from src.pages.header_page import HeaderPage
from src.pages.store_page import StorePage
from src.pages.product_detail_page import ProductDetailPage

class TestPortal():

    def test_store_link_leads_to_store_page(self,driver):
        header = HeaderPage(driver)
        header.click_store_menu()
        store_page = StorePage(driver)
        actual_header_text = store_page.get_header_text()
        assert actual_header_text == "Store"

    def test_store_link_url(self,driver):
        header = HeaderPage(driver)
        header.click_store_menu()
        assert driver.current_url == "https://askomdch.com/store/"

    def test_search_bar_in_store(self,driver):
        header = HeaderPage(driver)
        header.click_store_menu()
        store_page = StorePage(driver)
        store_page.search_item("store") #text is wrong on purpose to make it fail
        actual_header_text = store_page.get_header_text()
        assert actual_header_text == "Search results: “shoes”"

    def test_add_product_to_cart(self,driver):
        product_name = "Anchor Bracelet"
        header_page = HeaderPage(driver)
        header_page.click_store_menu()
        store_page = StorePage(driver)
        store_page.click_product_image(product_name)
        product_detail_page = ProductDetailPage(driver)
        product_detail_page.add_product_to_cart()
        header_page.display_cart_menu()
        actual_cart_prod_name = header_page.get_first_item_name_in_cart()
        assert actual_cart_prod_name == product_name

    @pytest.mark.skip(reason="Testing")
    def test_ignored_test():
        assert "a" == "b"
