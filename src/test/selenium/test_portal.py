import pytest
from src.pages.header_page import HeaderPage
from src.pages.store_page import StorePage
from src.pages.product_detail_page import ProductDetailPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.checkout_results import CheckoutResults
from src.utils.json_reader import JsonReader

class TestPortal():

    @pytest.mark.skip(reason="Testing")
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
        store_page.search_item("shoes")
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

    def test_select_third_option_in_checkout(self,driver):
        header_page = HeaderPage(driver)
        header_page.click_store_menu()
        store_page = StorePage(driver)
        store_page.click_on_first_available_product()
        product_detail_page = ProductDetailPage(driver)
        product_detail_page.add_product_to_cart()
        header_page.enter_to_cart()
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(driver)
        checkout_page.select_nth_country(3)
        current_country = checkout_page.get_current_selected_country()
        assert current_country == "Algeria", "Expected selected country does not match"

    @pytest.mark.flaky(reruns=1)
    def test_buy_a_product(self,driver):
        billing_address = JsonReader.get_test_file("billing_adress.json")
        header_page = HeaderPage(driver)
        header_page.click_store_menu()
        store_page = StorePage(driver)
        store_page.click_on_first_available_product()
        product_detail_page = ProductDetailPage(driver)
        product_detail_page.add_product_to_cart()
        header_page.enter_to_cart()
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(driver)
        checkout_page.set_billing_address(billing_address)
        checkout_page.place_order()
        checkout_results = CheckoutResults(driver)
        assert checkout_results.get_checkout_notice() == "Thank you. Your order has been received."

    @pytest.mark.skip(reason="Testing")
    def test_ignored_test(self):
        assert "a" == "b"
