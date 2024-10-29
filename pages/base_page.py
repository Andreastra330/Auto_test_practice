from selenium.webdriver import Keys
import os
from datetime import datetime
from .locators import *
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver,url):
        self.driver = driver
        self.url = url
        self.screenshot_dir = "F:/Zayavki"

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=60): # Элемент виден
        return wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))

    def elements_are_visible(self, locator, timeout=10): # Элементы видны
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=10): # Ищет по DOM дереву, чтобы до него не скролить
        return wait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=10): # Ищет по DOM дереву, чтобы до него не скролить все элементы
        return wait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10): # Элемент не виден
        return wait(self.driver,timeout).until(EC.invisibility_of_element(locator))

    def element_is_clickable(self, locator, timeout=10): # Элемент кликабельный
        return wait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self,locator):# Переместится к нужному элементу
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def send_keys(self, locator, keys):
        return self.driver.find_element(*locator).send_keys(keys)

    def click_element(self,locator):
        return self.driver.find_element(*locator).click()

    def send_key_arrow_up(self,locator):
        return self.driver.find_element(*locator).send_keys(Keys.ARROW_UP)

    def put_file(self,locator,path):
        return self.driver.find_element(*locator).send_keys(path)

    def take_screenshot(self, step_name):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{step_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
