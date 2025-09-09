from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.interactor import Interactor

class CheckoutPage(BasePage):

    FIRST_NAME_INPUT = (By.CSS_SELECTOR,"#billing_first_name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR,"#billing_last_name")
    ADDRESS_LINE_1_INPUT = (By.NAME,"billing_address_1")
    CITY_INPUT_INPUT = (By.NAME,"billing_city")
    POSTAL_CODE_INPUT = (By.NAME,"billing_postcode")
    COUNTRY_SELECT = (By.CSS_SELECTOR,"span.select2-selection span")
    COUNTRY_SELECT_RESULTS = (By.CSS_SELECTOR,"span.select2-results")
    STATE_SELECT = (By.ID,"select2-billing_state-container")
    EMAIL = (By.NAME,"billing_email")
    PLACE_ORDER_BTN = (By.ID,"place_order")

    def __init__(self, driver):
        super().__init__(driver)

    def get_current_selected_country(self):
        return Interactor.find_element(self.driver,self.COUNTRY_SELECT).text

    def select_nth_country(self,country_position: int):
        Interactor.find_element(self.driver,self.COUNTRY_SELECT).click()
        select_country_results = Interactor.find_element(self.driver, self.COUNTRY_SELECT_RESULTS)
        Interactor.select_nth_element(select_country_results,country_position)

    def set_billing_address(self,billing_address):
        self.enter_first_name(billing_address["firstName"])
        self.enter_last_name(billing_address["lastName"])
        self.enter_country(billing_address["country"])
        self.enter_address_line1(billing_address["addressLineOne"])
        self.enter_city(billing_address["city"])
        self.enter_state(billing_address["state"])
        self.enter_postal_code(billing_address["postalCode"])
        self.enter_email(billing_address["email"])

    def enter_first_name(self,first_name):
        Interactor.send_keys(self.driver,self.FIRST_NAME_INPUT,first_name)

    def enter_last_name(self,last_name):
        Interactor.send_keys(self.driver,self.LAST_NAME_INPUT,last_name)
        super().wait_for_blocking_overlays()

    def enter_country(self,country):
        Interactor.select_option(self.driver,self.COUNTRY_SELECT, country)
        super().wait_for_blocking_overlays()

    def enter_address_line1(self,address):
        Interactor.send_keys(self.driver,self.ADDRESS_LINE_1_INPUT,address)
        super().wait_for_blocking_overlays()

    def enter_city(self,city):
        Interactor.send_keys(self.driver,self.CITY_INPUT_INPUT,city)
        super().wait_for_blocking_overlays()

    def enter_state(self,state):
        Interactor.select_option(self.driver,self.STATE_SELECT, state)
        super().wait_for_blocking_overlays()

    def enter_postal_code(self,postal_code):
        Interactor.send_keys(self.driver,self.POSTAL_CODE_INPUT,postal_code)
        super().wait_for_blocking_overlays()

    def enter_email(self,email):
        Interactor.send_keys(self.driver,self.EMAIL,email)
        super().wait_for_blocking_overlays()

    def place_order(self):
        #Interactor.find_element(self.driver,self.PLACE_ORDER_BTN).click()
        Interactor.accurate_click(self.driver,self.PLACE_ORDER_BTN)
        super().wait_for_blocking_overlays()