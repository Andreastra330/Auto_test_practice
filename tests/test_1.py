import time

from pages.base_page import BasePage
from conftest import driver

def test_1(driver):
    page = BasePage(driver,"google.com")
    page.open()
    time.sleep(2)