from .base_page import *
import time
from .locators import *
current_id = None

class LoginPage(BasePage):
    locators = LoginLocators
    screenshot_dir = "F:/Zayavki/Методика 8"
    def take_screenshot(self, step_name):
        time.sleep(3)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{step_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def extract_current_id(self):
        global current_id
        url = self.driver.current_url  # Получаем текущий URL
        current_id = url.split('id=')[-1]
        return current_id

    def wait_until_reestr_is_loaded(self):
        self.find_element(MainButtonsLocators.REESTR)


    """Логинимся"""
    def login(self,login,password):
        self.find_element(self.locators.LOGIN).click()
        self.fill_input(self.locators.LOGIN,f"{login}")
        self.fill_input(self.locators.PASSWORD, f"{password}")
        self.element_is_clickable(self.locators.BUTTON_ENTER)
        self.click_element(self.locators.BUTTON_ENTER)

    def choice_need_razdel_gourp_reestr(self):
        self.element_is_clickable(RazdelLocators.BUTTON_RAZDEL)
        self.find_element(RazdelLocators.BUTTON_RAZDEL).click()
        self.element_is_clickable(RazdelLocators.CONFIG_RAZDEL)
        self.find_element(RazdelLocators.CONFIG_RAZDEL).click()
        self.element_is_clickable(RazdelLocators.ADMIN_GROUP)
        self.find_element(RazdelLocators.ADMIN_GROUP).click()
        self.element_is_clickable(RazdelLocators.DOC_REESTR)
        self.find_element(RazdelLocators.DOC_REESTR).click()
        self.wait_until_reestr_is_loaded()
        self.take_screenshot("3")

    def create_bo(self,naimenovanie,opisanie,data_nachala,data_okonchania,path_file,name_file,reestr):
        self.find_element(MainButtonsLocators.BUTTON_CREATE_IN_REESTR).click()
        self.take_screenshot("4")
        self.fill_input(ShablonDokumentaLocators.NAIMENOVANIE,f"{naimenovanie}")
        self.fill_input(ShablonDokumentaLocators.OPISANIE,f"{opisanie}")
        self.send_key_arrow_up(ShablonDokumentaLocators.DATA_NACHALA)
        self.fill_input(ShablonDokumentaLocators.DATA_NACHALA,f"{data_nachala}")
        self.send_key_arrow_up(ShablonDokumentaLocators.DATA_OKONCHANIA)
        self.fill_input(ShablonDokumentaLocators.DATA_OKONCHANIA,f"{data_okonchania}")
        self.find_element(ShablonDokumentaLocators.NAIMENOVANIE)
        self.take_screenshot("5")
        self.fill_input(ShablonDokumentaLocators.ENTER_FILE,f"{path_file}")
        self.fill_input(ShablonDokumentaLocators.SHABLON_BO,f"{reestr}")
        self.find_element_with_text(f"{reestr}").click()
        self.wait_until_file_load(name_file)
        self.take_screenshot("7")
        self.find_element(MainButtonsLocators.BUTTON_SAVE).click()
        self.take_screenshot("8")
        self.extract_current_id()
        self.find_element(MainButtonsLocators.BUTTON_CLOSE).click()
        self.wait_until_reestr_is_loaded()
        self.take_screenshot("9")

    def use_filter(self):
        self.find_element(FilterButtonsLocators.BUTTON_OPEN_FILTER).click()
        self.find_element(FilterButtonsLocators.BUTTON_SELECT_NAME_FIELD).click()
        self.find_element(FilterButtonsLocators.UID_BUTTON).click()
        self.fill_input(FilterButtonsLocators.BUTTON_VALUE_FIELD,current_id)
        time.sleep(5)
        self.find_element(FilterButtonsLocators.BUTTON_APPLY_FILTER).click()
        self.wait_until_reestr_is_loaded()

    def open_context_menu_and_click_edit(self):
        time.sleep(5)
        self.find_element(MainButtonsLocators.CONTEX_MENU_BUTTON).click()
        self.find_element(MainButtonsLocators.EDIT_BUTTON_IN_CONTEX_MENU).click()
        self.find_element(ShablonDokumentaLocators.NAIMENOVANIE)
        self.take_screenshot("10")

    def delete_file_and_load(self,path_file,name_file):
        self.find_element(ShablonDokumentaLocators.DELETE_FILE_BUTTON).click()
        self.find_element(ShablonDokumentaLocators.SHABLON_BO)
        self.take_screenshot("11")
        self.find_element(ShablonDokumentaLocators.ADD_FILE_WINDOW)
        self.fill_input(ShablonDokumentaLocators.ENTER_FILE,f"{path_file}")
        self.wait_until_file_load(name_file)
        time.sleep(5)
        self.take_screenshot("12")
        self.find_element(MainButtonsLocators.BUTTON_SAVE).click()
        self.take_screenshot("13")
        self.extract_current_id()
        self.find_element(MainButtonsLocators.BUTTON_CLOSE).click()
        self.wait_until_reestr_is_loaded()
        self.find_element(FilterButtonsLocators.DELETE_FILTER).click()
        self.take_screenshot("14")


