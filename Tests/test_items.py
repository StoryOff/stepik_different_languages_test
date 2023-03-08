import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_add_to_cart_button_exist(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    time.sleep(10)
