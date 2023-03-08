import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_add_to_cart_button_exist(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    # задержка во избежание лагов сервера
    time.sleep(2)
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert(len(add_to_cart_button) > 0), 'Кнопка добавления в корзину не найдена'
    time.sleep(30)
