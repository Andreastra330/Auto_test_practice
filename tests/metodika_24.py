import time
from pages.base_page import *
from pages.metodika_24_page import LoginPage
from conftest import driver


def test_24_method(driver):
    login_page = LoginPage(driver, 'https://kube-tsokr-config.nbt.dpr.norbit.ru/auth')
    login_page.open()
    login_page.login("AdminZakupa","Pass123$")
    login_page.razdel_for_admin_zakupa()
    login_page.use_filter()
    login_page.open_context_menu_and_click_vigruzka("TestOrlov")
    login_page.make_exit()


