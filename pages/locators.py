from selenium.webdriver.common.by import By
from .dynamic_locators import *

class LoginLocators:

    """Страница авторизации"""
    LOGIN = (By.CSS_SELECTOR, "input[id=text-field-Username]")
    PASSWORD = (By.CSS_SELECTOR, "input[id=password-field-Password]")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")


class RazdelLocators:
    BUTTON_RAZDEL = (By.CSS_SELECTOR, "div[data-testid='section']")
    SCROLL_RAZDEL = (By.CSS_SELECTOR, '[data-testid="containerScrollBar"]')
    CONFIG_RAZDEL = dynamic_razdel("Конфигурирование")
    ADMIN_GROUP = dynamic_group("Администрирование")
    DOC_REESTR = dynamic_reestr("Шаблоны документов")


class MainButtonsLocators:
    BUTTON_SAVE = (By.XPATH, "//*[@id='fab-check']")
    BUTTON_CLOSE = (By.XPATH, "//*[@id='fab-clear']")
    BUTTON_CREATE_IN_REESTR = (By.XPATH, "//*[@id='fab-create']")
    FIRST_ROW = (By.XPATH, '//div[@row-index="0"]')
    CONTEX_MENU_FIRST_ELEMENT_IN_REESTR = (By.XPATH, './/div[@col-id="context-menu-col"]//div[@data-test-title="Действия"]')
    REESTR = (By.CSS_SELECTOR, "div[class*='ag-row-no-animation']")
class ShablonDokumentaLocators:
    NAIMENOVANIE = (By.XPATH, "//*[@id='text-field-name']")
    OPISANIE = (By.XPATH, "//*[@id='text-area-field-description']")
    DATA_NACHALA = (By.XPATH, "//*[@id='date-field-startActivityDate']")
    DATA_OKONCHANIA = (By.XPATH, "//*[@id='date-field-endActivityDate']")
    FAIL = (By.XPATH, "//div[@class='uppy-Dashboard-AddFiles']")
    ENTER_FILE = (By.CSS_SELECTOR, "input[type='file']")
    SHABLON_BO = (By.XPATH, "//*[@id='search-select-field-boTemplateGuid']")
    NEED_SHABLON_BO = (By.XPATH, "//*[text() = 'Карточка закупки (kartochkazakupki)']")
    ACTUAL_IN_REEST = (By.XPATH, "//div[@class='ag-pinned-left-cols-container']")

class FilterButtonsLocators:
    BUTTON_OPEN_FILTER = (By.XPATH, "//button[@data-testid='add-condition']")
    BUTTON_SELECT_NAME_FIELD = (By.XPATH, "//*[@data-testid = 'arrow']")
    LIST_ITEMS_IN_FILTER = (By.XPATH, "//*[@data-test-id='virtuoso-item-list']")
    BUTTON_NAIMENOVANIE_IN_SELECT = (By.XPATH, "//div[@data-testid='containerScrollBar']//div[@data-testid='menuitem']//div[text()='Наименование']")
    BUTTON_VALUE_FIELD = (By.ID, "text-field-fieldValue")
    BUTTON_APPLY_FILTER = (By.XPATH, "//button[@data-testid='apply-filter']")

