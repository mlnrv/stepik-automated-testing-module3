import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_exists(browser):
    browser.get(link)
    time.sleep(5)
    btn_add_to_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert btn_add_to_basket != None 