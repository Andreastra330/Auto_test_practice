from locators.locator_1 import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = Locators()

    def fill_login(self):
        self.send_keys(self.locators.LOGIN,"Admin_doc")