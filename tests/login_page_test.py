import time

from selenium.webdriver.common.devtools.v127.fed_cm import click_dialog_button

from pages.login_page import LoginPage
from conftest import driver


def test_8_method(driver):
    login_page = LoginPage(driver,'https://kube-tsokr-config.nbt.dpr.norbit.ru/auth')
    login_page.open()
    login_page.wait_until_login_is_visible()
    login_page.fill_login()
    login_page.fill_password()
    time.sleep(1)
    login_page.click_login_button()
    login_page.wait_until_razdel_visible()
    time.sleep(1)
    login_page.click_razdel_button()
    time.sleep(10)