import pytest
from python.Pages.login_page import LoginPage
from python.Pages.start_page import StartPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def login_test(self):
        sp = StartPage(self.driver, self.wait)
        sp.click_login()
        lp = LoginPage(self.driver, self.wait)
        lp.input_data()

