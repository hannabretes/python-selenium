import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from python.Pages.base_page import BasePage


class LoginPage(BasePage):
    email_input = (By.XPATH, '//input[@placeholder="Email"]')
    password_input = (By.XPATH, '//input[@placeholder="Password"]')
    login_button = (By.XPATH, '//button[normalize-space()="Login"]')

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def input_data(self):
        self.do_send_keys(self.email_input, "test@wp.pl")
        self.do_send_keys(self.password_input, "Test1234!")
        self.do_click(self.login_button)

