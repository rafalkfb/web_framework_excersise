from selenium.webdriver.common.by import By


class Config:

    HOME_PAGE = "https://courses.letskodeit.com/"
    ALL_COURSES_PAGE = "https://courses.letskodeit.com/courses"
    LOGIN_EMAIL = "test@email.com"
    LOGIN_PASSWORD = "abcabc"

    # Navigation panel
    NAVIGATION_USER_TRIANGLE = (By.XPATH, "//a[@class='dynamic-link']//span[@class='caret']")
    NAVIGATION_HOME = (By.LINK_TEXT, "HOME")
    NAVIGATION_ALL_COURSES = (By.LINK_TEXT, "ALL COURSES")
    NAVIGATION_SUPPORT = (By.LINK_TEXT, "SUPPORT")
    NAVIGATION_MY_COURSES = (By.LINK_TEXT, "MY COURSES")

    # Login page locators
    LINK_TO_LOGIN_PAGE = (By.XPATH, "//a[@href='/login']")
    LOGIN_PAGE_EMAIL_FIELD = (By.ID, "email")
    LOGIN_PAGE_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")
    LOGIN_PAGE_INCORRECT_CREDENTIALS_INFO = (By.XPATH, "//span[contains(text(), 'username or password is invalid')]")

    # Courses locators
    COURSES_SEARCH_BOX = (By.CSS_SELECTOR, "input#search")  # "//input[@id='search']"
    COURSES_ALL_COURSES = (By.XPATH, "//h4[@class='dynamic-heading' and contains(text(), '{0}')]")
    COURSES_ENROLL_BUTTON = (By.XPATH, "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']")
    COURSES_CREDIT_CARD_NUM_FIELD = (By.XPATH, "//input[@name='cardnumber']")  # driver.switch_to.frame(0) ?
    COURSES_CREDIT_CARD_EXP_FIELD = (By.XPATH, "//input[@name='exp-date']")  # driver.switch_to.frame(1)
    COURSES_CREDIT_CARD_CVV = (By.XPATH, "//input[@name='cvc']")  # driver.switch_to.frame(2)
    COURSES_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'sp-buy')]")  # driver.switch_to.default_content()
    COURSES_ENROLL_ERROR_MESSAGE = (By.XPATH, "//span[normalize-space()='Your card number is invalid.']")