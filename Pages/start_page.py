import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from python.Pages.base_page import BasePage


class StartPage(BasePage):
    my_account_button = (By.XPATH,'//ul[@class="nav navbar-nav navbar-right hidden-sm go-left"]//a[@class="dropdown-toggle go-text-right"][normalize-space()="My Account"]')
    login_button = (By.XPATH, '//ul[@class="nav navbar-nav navbar-right hidden-sm go-left"]//ul[@class="nav navbar-nav navbar-side navbar-right sidebar go-left user_menu"]//li[@id="li_myaccount"]//ul[@class="dropdown-menu"]//li//a[@class="go-text-right"][normalize-space()="Login"]')

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def click_login(self):
        self.do_click(self.my_account_button)
        self.do_click(self.login_button)