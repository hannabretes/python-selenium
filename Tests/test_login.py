import pytest
import start_page
import login_page

@pytest.mark.usefixtures("setup")
class TestLogin():
    def login_test(self):
        sp = StartPage(self.driver, self.wait)
        sp.click_login()
        lp = LoginPage(self.driver, self.wait)
        lp.input_data()

