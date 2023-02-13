from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()
        