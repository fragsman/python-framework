from src.utils.interactor import Interactor

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    #common methods for all pages below this line
    def wait_for_blocking_overlays(self):
        Interactor.wait_for_blocking_overlays(self.driver)