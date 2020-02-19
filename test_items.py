import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_of_button_add_to_basket_in_different_languages(browser):
    browser.get(link)
    time.sleep(30)
    button_presence = 'yes'
    selector_for_button = ".btn-add-to-basket"
    try:
        browser.find_element_by_css_selector(selector_for_button)
    except:
        button_presence = 'no'
    assert button_presence == 'yes', f'На странице {link} отсутствует кнопка добавления товара в корзину с селектором {selector_for_button}'
