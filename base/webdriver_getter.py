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
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


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
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser == "opera":
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        elif self.browser == "remote":
            options = webdriver.ChromeOptions()
            options.set_capability("loggingPrefs", {'performance': 'ALL'})
            driver = webdriver.Remote(command_executor="127.0.0.1:4444", options=options)
        elif self.browser == "noimages":
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            # driver = webdriver.Chrome(options=chrome_options)
        elif self.browser == "headless":
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
        driver.get(base_url)
        return driver
