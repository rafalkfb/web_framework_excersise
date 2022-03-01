import pytest
from base.browser_factory import BrowserFactory
from pages.home.login_page import LoginPage
from configfiles.config_data import Config


@pytest.fixture()
def set_up():
    # print("Running general setup")
    yield
    # print("Running general teardown")


@pytest.fixture(scope="class")  # read about different scopes
def one_time_set_up(request, browser):
    # print("Running general onetime setup")
    driver = BrowserFactory().webdriver_instance(browser)
    driver.get(Config.HOME_PAGE)
    log_page = LoginPage(driver)
    log_page.login(Config.LOGIN_EMAIL, Config.LOGIN_PASSWORD)
    if request.cls is not None:      # read more about it
        request.cls.driver = driver

    yield driver
    driver.quit()
    # print("Running general onetime teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os_type", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='session')
def os_type(request):
    return request.config.getoption("--os_type")
