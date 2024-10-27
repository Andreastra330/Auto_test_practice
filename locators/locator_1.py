from selenium.webdriver.common.by import By


class Locators:

    #Страница авторизации
    LOGIN = (By.CSS_SELECTOR, "input[id=text-field-Username]")
    PASSWORD = (By.CSS_SELECTOR, "input[id=password-field-Password]")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[text()=Войти]")


