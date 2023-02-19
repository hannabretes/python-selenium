from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        self.wait.until(ec.visibility_of_element_located(locator)).send_keys(text)
