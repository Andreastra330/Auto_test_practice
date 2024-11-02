from .base_page import BasePage
import time
from .locators import *


class LoginPage(BasePage):
    locators = LoginLocators
    """Логинимся"""
    def wait_until_login_is_visible(self):
        self.element_is_visible(self.locators.LOGIN)
    def fill_login(self):
        self.send_keys(self.locators.LOGIN,"Admin_doc")
    def fill_password(self):
        self.send_keys(self.locators.PASSWORD, "Pass123$")
    def wait_until_enter_is_visible(self):
        self.element_is_visible(self.locators.BUTTON_ENTER)
    def click_login_button(self):
        self.click_element(self.locators.BUTTON_ENTER)

    def login(self,login,password):
        self.find_element(self.locators.LOGIN).click()
        self.fill_input(self.locators.LOGIN,f"{login}")
        self.fill_input(self.locators.PASSWORD, f"{password}")
        self.element_is_clickable(self.locators.BUTTON_ENTER)
        self.click_element(self.locators.BUTTON_ENTER)

    def choice_need_razdel_gourp_reestr(self,razdel,group,reestr):
        self.element_is_clickable(RazdelLocators.BUTTON_RAZDEL)
        self.find_element(RazdelLocators.BUTTON_RAZDEL).click()
        self.element_is_clickable(RazdelLocators.CONFIG_RAZDEL)
        self.find_element(RazdelLocators.CONFIG_RAZDEL).click()
        self.element_is_clickable(RazdelLocators.ADMIN_GROUP)
        self.find_element(RazdelLocators.ADMIN_GROUP).click()
        self.element_is_clickable(RazdelLocators.DOC_REESTR)
        self.find_element(RazdelLocators.DOC_REESTR).click()

    def create_bo(self,naimenovanie,opisanie,data_nachala,data_okonchania,path_file,name_file,reestr):
        self.find_element(MainButtonsLocators.BUTTON_CREATE_IN_REESTR).click()
        self.fill_input(ShablonDokumentaLocators.NAIMENOVANIE,f"{naimenovanie}")
        self.fill_input(ShablonDokumentaLocators.OPISANIE,f"{opisanie}")
        self.send_key_arrow_up(ShablonDokumentaLocators.DATA_NACHALA)
        self.fill_input(ShablonDokumentaLocators.DATA_NACHALA,f"{data_nachala}")
        self.send_key_arrow_up(ShablonDokumentaLocators.DATA_OKONCHANIA)
        self.fill_input(ShablonDokumentaLocators.DATA_OKONCHANIA,f"{data_okonchania}")
        self.fill_input(ShablonDokumentaLocators.ENTER_FILE,f"{path_file}")
        self.fill_input(ShablonDokumentaLocators.SHABLON_BO,f"{reestr}")
        self.find_element_with_text(f"{reestr}").click()
        self.wait_until_file_load(name_file)
       # self.find_element(MainButtonsLocators.BUTTON_SAVE).click()
       # self.find_element(MainButtonsLocators.BUTTON_CLOSE).click()

    def wait_until_reestr_is_loaded(self):
        self.find_element(MainButtonsLocators.REESTR)

    """Раздел + реестр"""
    def wait_until_razdel_visible(self):
        self.element_is_visible(self.locators.BUTTON_RAZDEL)
    def click_razdel_button(self):
        self.click_element(self.locators.BUTTON_RAZDEL)
    def wait_until_need_razdel_visible(self):
        self.element_is_visible(self.locators.BUTTON_NEED_RAZDEL)
    def click_need_razdel_button(self):
        self.click_element(self.locators.BUTTON_NEED_RAZDEL)
    def wait_until_group_reestr_is_visible(self):
        self.element_is_visible(self.locators.BUTTON_GROUP_REESTR)
    def click_group_reestr_button(self):
        self.click_element(self.locators.BUTTON_GROUP_REESTR)
    def wait_until_reestr_is_visible(self):
        self.element_is_visible(self.locators.BUTTON_REESTR)
    def click_reestr_button(self):
        self.click_element(self.locators.BUTTON_REESTR)
    def wait_until_button_create_in_reestr_visible(self):
        self.element_is_visible(self.locators.BUTTON_CREATE_IN_REESTR)
    def wait_until_actual_in_reestr(self):
        self.element_is_visible(self.locators.ACTUAL_IN_REEST)
    """Создать"""
    def click_button_create_in_reestr_button(self):
        self.click_element(self.locators.BUTTON_CREATE_IN_REESTR)
    """Заполнение полей"""
    def wait_until_naimenovanie_visible(self):
        self.element_is_visible(self.locators.NAIMENOVANIE)
    def fill_naimenovanie(self):
        self.send_keys(self.locators.NAIMENOVANIE,"Test_Orlov")
    def fill_opisanie(self):
        self.send_keys(self.locators.OPISANIE,"Proverka")
    def arrow_up_data_nachala(self):
        self.send_key_arrow_up(self.locators.DATA_NACHALA)
    def arrow_up_data_okonchania(self):
            self.send_key_arrow_up(self.locators.DATA_OKONCHANIA)
    def fill_data_nachala(self):
        self.send_keys(self.locators.DATA_NACHALA,"29102024")
    def fill_data_okonchania(self):
        self.send_keys(self.locators.DATA_OKONCHANIA,"31102024")
    def put_my_file(self):
        self.put_file(self.locators.ENTER_FILE,"F:/Zayavki/FD.docx")
    def scroll_to_fail(self):
        self.go_to_element(self.locators.FAIL)
    def fill_shablon_bo(self):
        self.send_keys(self.locators.SHABLON_BO,"Карточка закупки")
    def click_need_element_in_shablon_bo(self):
        self.click_element(self.locators.NEED_SHABLON_BO)
    def check_button_save_clickable(self):
        self.element_is_clickable(self.locators.BUTTON_SAVE)
    def click_button_save_in_bo(self):
        self.click_element(self.locators.BUTTON_SAVE)
    def check_button_close_clickable(self):
        self.element_is_clickable(self.locators.BUTTON_CLOSE)
    def click_button_close_in_bo(self):
        self.click_element(self.locators.BUTTON_CLOSE)
    def click_on_button_open_filter_in_reestr(self ):
        self.click_element(self.locators.BUTTON_OPEN_FILTER)
    def wait_until_load_select_in_filter(self):
        self.element_is_visible(self.locators.BUTTON_SELECT_NAME_FIELD)
    def click_button_select_in_filter(self):
        self.click_element(self.locators.BUTTON_SELECT_NAME_FIELD)
    def wait_until_load_list_itmes(self):
        self.element_is_visible(self.locators.LIST_ITEMS_IN_FILTER)
    def wait_until_naimenovanie_clickable(self):
        self.element_is_clickable(self.locators.BUTTON_NAIMENOVANIE_IN_SELECT)
    def click_naimenovanie_in_select(self):
        self.click_element(self.locators.BUTTON_NAIMENOVANIE_IN_SELECT)
    def wait_until_value_in_filter(self):
        self.element_is_visible(self.locators.BUTTON_VALUE_FIELD)
    def fill_until_value_in_filter(self):
        self.send_keys(self.locators.BUTTON_VALUE_FIELD,"Test_Orlov")
    def click_apply_filter(self):
        self.click_element(self.locators.BUTTON_APPLY_FILTER)
    def wait_until_checkbox_in_reestr(self):
        self.element_is_visible(self.locators.CONTEX_MENU_FIRST_ELEMENT_IN_REESTR)
    def click_on_checkbox_in_reestr(self):
        self.click_element(self.locators.CONTEX_MENU_FIRST_ELEMENT_IN_REESTR)
