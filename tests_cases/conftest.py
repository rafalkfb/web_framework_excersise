import pytest
from base.webdriver_getter import WebDriverCreate
from pages.home.login_page import LoginPage


@pytest.fixture()
def set_up():
    # print("Running general setup")
    yield
    # print("Running general teardown")


@pytest.fixture(scope="class")  # read about different scopes
def one_time_set_up(request, browser):
    # print("Running general onetime setup")
    wdc = WebDriverCreate(browser)
    driver = wdc.get_webdriver_instance()
    log_page = LoginPage(driver)
    log_page.login("test@email.com", "abcabc")
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
