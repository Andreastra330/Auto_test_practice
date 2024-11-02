from selenium.webdriver.common.by import By

def dynamic_razdel(button_text):
    return (By.XPATH, f"//div[@data-testid='containerScrollBar']//span[text()='{button_text}']")

def dynamic_group(button_text):
    return(By.XPATH, f"//*[text() = '{button_text}']")

def dynamic_reestr(button_text):
    return (By.XPATH, f"//*[text() = '{button_text}']")