import time

from selenium.webdriver.common.devtools.v127.fed_cm import click_dialog_button

from pages.login_page import LoginPage
from conftest import driver


def test_8_method(driver):
    login_page = LoginPage(driver,'https://kube-tsokr-config.nbt.dpr.norbit.ru/auth')
    login_page.open()
    login_page.login("Admin_doc","Pass123$")
    login_page.choice_need_razdel_gourp_reestr("Конфигурирование","Администрирование","Шаблоны документов")
    login_page.wait_until_reestr_is_loaded()
    login_page.create_bo("Orlov_auto_test","test","02112024","06112024","F:/Zayavki/FD.docx","FD.docx","Карточка закупки (kartochkazakupki)")
    #login_page.wait_until_reestr_is_loaded()
    time.sleep(2)


