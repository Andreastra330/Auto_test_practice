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
    PROVEDENIE = dynamic_razdel("Проведение закупки")
    ZAKUPKI = dynamic_group("Закупки")
    KARTOCHKA_ZAKUPKI = dynamic_reestr("Карточка закупки")

class MainButtonsLocators:
    BUTTON_SAVE = (By.XPATH, "//*[@id='fab-check']")
    BUTTON_CLOSE = (By.XPATH, "//*[@id='fab-clear']")
    BUTTON_CREATE_IN_REESTR = (By.XPATH, "//*[@id='fab-create']")
    FIRST_ROW = (By.XPATH, '//div[@row-index="0"]')
    CONTEX_MENU_BUTTON = (By.XPATH, './/div[@col-id="context-menu-col"]//div[@data-test-title="Действия"]')
    EDIT_BUTTON_IN_CONTEX_MENU = (By.XPATH, '//ul[@data-testid="context-menu-buttons"]//li[text()="Изменить"]')
    REESTR = (By.CSS_SELECTOR, "div[class*='ag-row-no-animation']")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "div[data-testid='profile']")
    EXIT_BUTTON = (By.XPATH, "//*[@data-testid = 'menuitem']//*[text() = 'Выйти']")
    VIGRUZKA_BUTTON_IN_CONTEX_MENU = (By.XPATH, '//ul[@data-testid="context-menu-buttons"]//li[text()="Выгрузить по шаблону"]')
    INPUT_SHABLON_DOKUMENTA = (By.NAME, "search-documentTemplateId")
    NOT_FOUND = (By.XPATH, '//span[text()="Не найдено!"]')
    NOMER_ZAKUPKI = (By.XPATH, "//*[text() = 'Номер карточки закупки']")
    
class ShablonDokumentaLocators:
    NAIMENOVANIE = (By.XPATH, "//*[@id='text-field-name']")
    OPISANIE = (By.XPATH, "//*[@id='text-area-field-description']")
    DATA_NACHALA = (By.XPATH, "//*[@id='date-field-startActivityDate']")
    DATA_OKONCHANIA = (By.XPATH, "//*[@id='date-field-endActivityDate']")
    FAIL = (By.XPATH, "//div[@class='uppy-Dashboard-AddFiles']")
    ENTER_FILE = (By.CSS_SELECTOR, "input[type='file']")
    SHABLON_BO = (By.XPATH, "//*[@id='search-select-field-boTemplateGuid']")
    NEED_SHABLON_BO = (By.XPATH, "//*[text() = 'Карточка закупки (kartochkazakupki)']")
    DELETE_FILE_BUTTON = (By.CSS_SELECTOR, "div[data-testid='delete-file']")
    ADD_FILE_WINDOW = (By.CSS_SELECTOR, "div[class='uppy-Dashboard-AddFiles']")
    ACTUALNOST = (By.XPATH, '//span[@data-testid="checkbox"]')
    FOR_CLICK =  (By.XPATH, "//label[@for='field-0']")

class FilterButtonsLocators:
    BUTTON_OPEN_FILTER = (By.XPATH, "//button[@data-testid='add-condition']")
    BUTTON_SELECT_NAME_FIELD = (By.XPATH, "//*[@data-testid = 'arrow']")
    LIST_ITEMS_IN_FILTER = (By.XPATH, "//*[@data-test-id='virtuoso-item-list']")
    BUTTON_NAIMENOVANIE_IN_SELECT = (By.XPATH, "//div[@data-testid='containerScrollBar']//div[@data-testid='menuitem']//div[text()='Наименование']")
    UID_BUTTON = (By.XPATH, "//div[@data-testid='containerScrollBar']//div[@data-testid='menuitem']//div[text()='Уникальный идентификатор']")
    BUTTON_VALUE_FIELD = (By.ID, "text-field-fieldValue")
    BUTTON_APPLY_FILTER = (By.XPATH, "//button[@data-testid='apply-filter']")
    INPUT_FILTER = (By.XPATH,"//*[@id='search-select-field-fieldName']")
    DELETE_FILTER = (By.CSS_SELECTOR, "button[data-testid='clear-filter']")
