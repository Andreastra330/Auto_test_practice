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
    login_page.take_screenshot("login")
    login_page.click_login_button()
    login_page.wait_until_razdel_visible()
    login_page.click_razdel_button()
    login_page.wait_until_need_razdel_visible()
    login_page.click_need_razdel_button()
    login_page.wait_until_group_reestr_is_visible()
    login_page.click_group_reestr_button()
    login_page.wait_until_reestr_is_visible()
    login_page.click_reestr_button()
    login_page.wait_until_button_create_in_reestr_visible()
    login_page.take_screenshot("create")
    login_page.click_button_create_in_reestr_button()
    login_page.wait_until_naimenovanie_visible()
    login_page.fill_naimenovanie()
    login_page.fill_opisanie()
    login_page.arrow_up_data_nachala()
    login_page.fill_data_nachala()
    login_page.arrow_up_data_okonchania()
    login_page.fill_data_okonchania()
    login_page.take_screenshot("opisanie")
    login_page.scroll_to_fail()
    login_page.put_my_file()
    login_page.fill_shablon_bo()
    login_page.click_need_element_in_shablon_bo()
    login_page.take_screenshot("fill")
    time.sleep(10)
    login_page.check_button_save_clickable()
    login_page.click_button_save_in_bo()
    login_page.check_button_close_clickable()
    login_page.click_button_close_in_bo()
    time.sleep(10)