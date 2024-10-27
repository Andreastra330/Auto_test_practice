import time

from pages.login_page import LoginPage


class LoginPageTest:
    class Test:
        def test_login_page(self,driver):
            page = LoginPage(driver,'https://kube-tsokr-config.nbt.dpr.norbit.ru/auth')
            page.open()
            time.sleep(5)
            page.fill_login()
            time.sleep(5)