import time



from conftest import driver
from pages.login_page import LoginPage



def test_1(driver):
    page = LoginPage(driver,'https://kube-tsokr-config.nbt.dpr.norbit.ru/auth')
    page.open()
    time.sleep(2)

    time.sleep(10)

