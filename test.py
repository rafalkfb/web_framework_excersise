from selenium import webdriver


def main():
    options = webdriver.ChromeOptions()
    options.set_capability("loggingPrefs", {'performance': 'ALL'})
    driver = webdriver.Remote(command_executor="localhost:4444", options=options)
    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()


if __name__ == "__main__":
    main()
