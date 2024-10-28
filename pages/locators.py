from selenium.webdriver.common.by import By


class LoginLocators:

    """Страница авторизации"""
    LOGIN = (By.CSS_SELECTOR, "input[id=text-field-Username]")
    PASSWORD = (By.CSS_SELECTOR, "input[id=password-field-Password]")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    BUTTON_RAZDEL = (By.CSS_SELECTOR, '[data-testid="section"]')
    BUTTON_NEED_RAZDEL = (By.XPATH, "//*[text() = 'Конфигурирование']")
    BUTTON_GROUP_REESTR = (By.XPATH, "//*[text() = 'Администрирование']")
    BUTTON_REEST = (By.XPATH, "//*[text() = 'Шаблоны документов']")


