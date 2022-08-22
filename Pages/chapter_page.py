from webdriver import Browser
from .base_page import BasePage
from Locators.chapter_locators import ChapterLocators
from Elements.button import Button
from logger import CustomLogger

LOGGER = CustomLogger.get_logger(__name__)


class ChapterPage(BasePage):

    def __init__(self, wait_time):
        super().__init__(wait_time)
        self.NEXT_BTN = Button(
            ChapterLocators.CHAPTER_NEXT_BTN, 'Next Chapter Button', wait_time)

    def go_to_next_chapter(self):
        LOGGER.info('Getting next chapter')
        self.NEXT_BTN.do_click()

    def verify_page(self):
        return self.verify_page_by_element(ChapterLocators.CHAPTER_NEXT_BTN)
