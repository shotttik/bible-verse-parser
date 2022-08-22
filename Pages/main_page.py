from webdriver import Browser
from .base_page import BasePage
from Locators.main_locators import MainLocators
from Elements.button import Button


class MainPage(BasePage):

    def __init__(self, wait_time, start_url):
        super().__init__(wait_time)
        self.start_url = start_url

    def verify_page(self):
        return self.verify_page_by_element(MainLocators.HOME_ICON)

    def go_to_parsing_page(self):
        Browser.getInstance().get(self.start_url)
