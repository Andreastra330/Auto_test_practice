from telnetlib import SEND_URL

from .base_page import *
import time
from .locators import *
current_id = None

class LoginPage(BasePage):
    locators = LoginLocators


    def extract_current_id(self):
        global current_id
        url = self.driver.current_url  # Получаем текущий URL
        current_id = url.split('id=')[-1]
        return current_id

    def wait_until_reestr_is_loaded(self):
        self.element_is_clickable(MainButtonsLocators.NOMER_ZAKUPKI)
        self.take_screenshot("Реестр")

    """Логинимся"""

    def login(self, login, password):
        self.find_element(self.locators.LOGIN).click()
        self.fill_input(self.locators.LOGIN, f"{login}")
        self.fill_input(self.locators.PASSWORD, f"{password}")
        self.element_is_clickable(self.locators.BUTTON_ENTER)
        self.click_element(self.locators.BUTTON_ENTER)

    def razdel_for_admin_doc(self):
        self.element_is_clickable(RazdelLocators.BUTTON_RAZDEL)
        self.find_element(RazdelLocators.BUTTON_RAZDEL).click()
        self.element_is_clickable(RazdelLocators.CONFIG_RAZDEL)
        self.find_element(RazdelLocators.CONFIG_RAZDEL).click()
        self.element_is_clickable(RazdelLocators.ADMIN_GROUP)
        self.find_element(RazdelLocators.ADMIN_GROUP).click()
        self.element_is_clickable(RazdelLocators.DOC_REESTR)
        self.find_element(RazdelLocators.DOC_REESTR).click()
        self.wait_until_reestr_is_loaded()

    def razdel_for_admin_zakupa(self):
        self.element_is_clickable(RazdelLocators.BUTTON_RAZDEL)
        self.find_element(RazdelLocators.BUTTON_RAZDEL).click()
        self.element_is_clickable(RazdelLocators.PROVEDENIE)
        self.find_element(RazdelLocators.PROVEDENIE).click()
        self.element_is_clickable(RazdelLocators.ZAKUPKI)
        self.find_element(RazdelLocators.ZAKUPKI).click()
        self.element_is_clickable(RazdelLocators.KARTOCHKA_ZAKUPKI)
        self.find_element(RazdelLocators.KARTOCHKA_ZAKUPKI).click()
        time.sleep(10)

    def create_bo(self, naimenovanie, opisanie, data_nachala, data_okonchania, path_file, name_file, reestr):
        self.find_element(MainButtonsLocators.BUTTON_CREATE_IN_REESTR).click()
        self.fill_input(ShablonDokumentaLocators.NAIMENOVANIE, f"{naimenovanie}")
        self.fill_input(ShablonDokumentaLocators.OPISANIE, f"{opisanie}")
        self.send_key_arrow_up(ShablonDokumentaLocators.DATA_NACHALA)
        self.fill_input(ShablonDokumentaLocators.DATA_NACHALA, f"{data_nachala}")
        self.send_key_arrow_up(ShablonDokumentaLocators.DATA_OKONCHANIA)
        self.fill_input(ShablonDokumentaLocators.DATA_OKONCHANIA, f"{data_okonchania}")
        self.fill_input(ShablonDokumentaLocators.SHABLON_BO, f"{reestr}")
        self.find_element_with_text(f"{reestr}").click()
        self.fill_input(ShablonDokumentaLocators.ENTER_FILE, f"{path_file}")
        self.wait_until_file_load(name_file)
        self.take_screenshot("Файл загружен")
        self.find_element(MainButtonsLocators.BUTTON_SAVE).click()
        time.sleep(2)
        self.extract_current_id()
        self.value_false(ShablonDokumentaLocators.ACTUALNOST)

    def make_exit(self):
        self.find_element(MainButtonsLocators.PROFILE_BUTTON).click()
        self.find_element(MainButtonsLocators.EXIT_BUTTON).click()

    def use_filter(self):
        self.find_element(FilterButtonsLocators.BUTTON_OPEN_FILTER).click()
        self.fill_input(FilterButtonsLocators.BUTTON_SELECT_NAME_FIELD,"Уникальный идентификатор")
        self.find_element(FilterButtonsLocators.UID_BUTTON).click()
        self.fill_input(FilterButtonsLocators.BUTTON_VALUE_FIELD, "3685980")
        time.sleep(1)
        self.find_element(FilterButtonsLocators.BUTTON_APPLY_FILTER).click()
        time.sleep(10)

    def open_context_menu_and_click_vigruzka(self,naimenovanie):
        self.find_element(MainButtonsLocators.CONTEX_MENU_BUTTON).click()
        self.find_element(MainButtonsLocators.VIGRUZKA_BUTTON_IN_CONTEX_MENU).click()
        self.fill_input(MainButtonsLocators.INPUT_SHABLON_DOKUMENTA,f"{naimenovanie}")
        self.not_found(MainButtonsLocators.NOT_FOUND)
        #self.find_element(MainButtonsLocators.PROFILE_BUTTON).click()


