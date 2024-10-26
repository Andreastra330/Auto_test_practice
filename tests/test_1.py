import time

from pages.base_page import BasePage
from conftest import browser

def test_1(browser):
    page = BasePage(browser,"google.com")
    page.open()
    time.sleep(2)