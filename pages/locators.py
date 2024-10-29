from selenium.webdriver.common.by import By


class LoginLocators:

    """Страница авторизации"""
    LOGIN = (By.CSS_SELECTOR, "input[id=text-field-Username]")
    PASSWORD = (By.CSS_SELECTOR, "input[id=password-field-Password]")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    BUTTON_RAZDEL = (By.CSS_SELECTOR, "div[data-testid='section']")

    SCROLL_RAZDEL = (By.CSS_SELECTOR, '[data-testid="containerScrollBar"]')
    BUTTON_NEED_RAZDEL = (By.XPATH, "//div[@data-testid='containerScrollBar']//span[text()='Конфигурирование']")
    BUTTON_GROUP_REESTR = (By.XPATH, "//*[text() = 'Администрирование']")
    BUTTON_REESTR = (By.XPATH, "//*[text() = 'Шаблоны документов']")
    BUTTON_CREATE_IN_REESTR = (By.XPATH, "//*[@id='fab-create']")

    NAIMENOVANIE = (By.XPATH, "//*[@id='text-field-name']")
    OPISANIE = (By.XPATH, "//*[@id='text-area-field-description']")
    DATA_NACHALA = (By.XPATH, "//*[@id='date-field-startActivityDate']")
    DATA_OKONCHANIA = (By.XPATH, "//*[@id='date-field-endActivityDate']")
    FAIL = (By.XPATH, "//div[@class='uppy-Dashboard-AddFiles']")
    ENTER_FILE = (By.CSS_SELECTOR, "input[type='file']")
    SHABLON_BO = (By.XPATH, "//*[@id='search-select-field-boTemplateGuid']")
    NEED_SHABLON_BO = (By.XPATH, "//*[text() = 'Карточка закупки (kartochkazakupki)']")


