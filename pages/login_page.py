from .base_page import BasePage
import time
from .locators import *


class LoginPage(BasePage):
    locators = LoginLocators

    def wait_until_login_is_visible(self):
        self.element_is_visible(self.locators.LOGIN)

    def fill_login_and_password(self):
        self.send_keys(self.locators.LOGIN,"Admin_doc")

    def fill_password(self):
        self.send_keys(self.locators.PASSWORD,"Pass123$")