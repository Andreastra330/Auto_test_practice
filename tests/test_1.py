import time

from pages.base_page import BasePage


def test_1(browser):
    page = BasePage(browser,"google.com")
    page.open()
    time.sleep(2)