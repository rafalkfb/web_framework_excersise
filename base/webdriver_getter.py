"""
@package base

WebDriver Create class implementation
It creates a webdriver instance based on a browser configurations

Example:
    wdc = WebDriverCreate(browser)
    wdc.get_webdriver_instance()
        or for clearance
    driver = wdc.get_webdriver_instance()
"""

from selenium import webdriver


class WebDriverCreate:

    def __init__(self, browser):
        """
        Initiates WebDriverCreate class
        :param browser:
        :return None:
        """
        self.browser = browser

    """
            Set chrome driver and others environment based on OS

            chromedriver = "C:/.../chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)

            PREFERRED: Set the path on the machine where browser will be executed
    """

    def get_webdriver_instance(self):
        """
        Get WebDriver Instance based on the browser provided by user as command argument
        by default it's Chromedriver

        :return: 'WebDriver instance'
        """
        base_url = "https://courses.letskodeit.com/"
        if self.browser == "edge":
            driver = webdriver.Edge()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        # setting driver implicit time out for an element
        driver.implicitly_wait(5)
        # maximize the window
        driver.maximize_window()
        # loading browser with App URL
        driver.get(base_url)
        return driver
