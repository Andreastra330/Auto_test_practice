from .base_page import BasePage
import time
from .locators import *


class LoginPage(BasePage):
    locators = LoginLocators

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
    def wait_until_razdel_visible(self):
        self.element_is_visible(self.locators.BUTTON_RAZDEL)
    def click_razdel_button(self):
        self.click_element(self.locators.BUTTON_RAZDEL)