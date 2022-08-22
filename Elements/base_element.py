from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver import Browser
import logging
LOGGER = logging.getLogger(__name__)


class BaseElement:

    def __init__(self, by_locator, name, wait_time):
        self.by_locator = by_locator
        self.name = name
        self.wait_time = wait_time
        self.actions = ActionChains(Browser.getInstance())

    def do_click(self):
        LOGGER.info(f'Click on element {self.name}')
        WebDriverWait(Browser.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located(self.by_locator)).click()

    def do_click_with_action(self):
        LOGGER.info(f'Click with action on element {self.name}')
        el = WebDriverWait(Browser.getInstance(), self.wait_time).until(
            EC.presence_of_element_located(self.by_locator))
        self.actions.move_to_element(el).click().perform()

    def wait_for_element_to_dissapear(self):
        LOGGER.info(f'wait to dissapear {self.name}')
        WebDriverWait(Browser.getInstance(), self.wait_time).until(
            EC.invisibility_of_element_located(self.by_locator))

    def get_element_text(self) -> str:
        LOGGER.info(f'Get text from element {self.name}')
        element = WebDriverWait(Browser.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located(self.by_locator)
        )
        return element.text

    def get_element_attribute_value(self, attribute: str):
        LOGGER.info(f'Get attribute value from element {self.name}')
        element = WebDriverWait(Browser.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located(self.by_locator)
        )
        val = element.get_attribute(attribute)
        return int(val) if val is not None else None

    def scroll_to_element(self):
        LOGGER.info(f'Scroll to element {self.name}')
        element = WebDriverWait(Browser.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located(self.by_locator)
        )
        Browser.getInstance().execute_script(
            "arguments[0].scrollIntoView();", element)

    # if we have too much elements with same locator
    def click_element_find_by_el_name(self):
        LOGGER.info(f'Clicking specific element {self.name} by text')
        elements = WebDriverWait(Browser.getInstance(), self.wait_time).until(
            EC.visibility_of_all_elements_located(self.by_locator)
        )
        next(element for element in elements if element.text == self.name).click()
