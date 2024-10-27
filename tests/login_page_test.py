import time

from pages.login_page import LoginPage
from conftest import driver


def test_1(driver):
    login_page = LoginPage(driver,'https://kube-tsokr-config.nbt.dpr.norbit.ru/auth')
    login_page.open()
    login_page.wait_until_login_is_visible()
    login_page.fill_login_and_password()
    login_page.fill_password()
    time.sleep(10)