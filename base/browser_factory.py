"""
@package base

WebDriver Create class implementation
It creates a webdriver instance based on a browser configurations

Example:
    wdc = BrowserFactory(browser)
    wdc.get_webdriver_instance()
        or for clearance
    driver = wdc.get_webdriver_instance()
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


class BrowserFactory:

    @staticmethod
    def webdriver_instance(browser):
        """
        Get WebDriver Instance based on the browser provided by user as command argument
        by default it's Chromedriver

        :return: 'WebDriver instance'
        """
        if browser == "edge":
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "opera":
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        elif browser == "remote":
            options = webdriver.ChromeOptions()
            options.set_capability("loggingPrefs", {'performance': 'ALL'})
            driver = webdriver.Remote(command_executor="127.0.0.1:4444", options=options)
        elif browser == "docker-remote":
            options = webdriver.ChromeOptions()
            options.set_capability("loggingPrefs", {'performance': 'ALL'})
            driver = webdriver.Remote(command_executor="http://selenium-hub:4444", options=options)
        elif browser == "noimages":
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            # driver = webdriver.Chrome(options=chrome_options)
        elif browser == "headless":
            chrome_options = webdriver.ChromeOptions()
            # prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_argument("--headless")
            chrome_options.add_argument('--lang=en')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        # setting driver implicit time out for an element
        driver.implicitly_wait(3)
        # maximize the window
        driver.maximize_window()
        # loading browser with App URL
        return driver
