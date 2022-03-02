import pytest
from pages.home.login_page import LoginPage
import unittest
from utilities.checkteststatus import CheckTestStatus
from pages.home.navigation_panel import NavigationPanel
from configfiles.config_data import Config


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.base_url = "https://courses.letskodeit.com/"  # check if it can be moved to fixture or conftest
        self.log_page = LoginPage(self.driver)
        self.test_status = CheckTestStatus(self.driver)
        self.navigation_panel = NavigationPanel(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.driver.get(self.base_url)
        self.log_page.login(Config.LOGIN_EMAIL, Config.LOGIN_PASSWORD)

        # verify page title
        result = self.log_page.verify_title_match("My Courses")
        self.test_status.mark(result, "Title is incorrect")  # message should say what was incorrect
        # verify successful login
        result = self.log_page.verify_successful_login()
        self.test_status.mark_final("test_valid_login", result, "Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        # self.driver.get(self.base_url)
        self.navigation_panel.click_logout()
        self.log_page.login("test@email.com", "assbcabc")

        assert self.log_page.verify_login_failed()
