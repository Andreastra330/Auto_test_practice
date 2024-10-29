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
        self.put_file(self.locators.ENTER_FILE,"C:/Zayvki/FD.docx")
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


