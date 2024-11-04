import time
from pages.base_page import *
from pages.login_page import LoginPage
from conftest import driver


def test_8_method(driver):
    login_page = LoginPage(driver, 'https://kube-tsokr-config.nbt.dpr.norbit.ru/auth')
    login_page.open()
    login_page.login("Admin_doc", "Pass123$")
    login_page.choice_need_razdel_gourp_reestr()
    login_page.create_bo("ПГК, шаблон тест", "test", "02112024", "06112024", "F:/Zayavki/FD.docx", "FD.docx","Карточка закупки (kartochkazakupki)")
    login_page.use_filter()
    login_page.open_context_menu_and_click_edit()
    login_page.delete_file_and_load("F:/Zayavki/FD2.docx", "FD2.docx")
    time.sleep(2)



