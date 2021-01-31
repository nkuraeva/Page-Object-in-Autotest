import pytest
import time
from selenium import webdriver
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.base_page import BasePage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.right_name_in_basket()
    page.right_price_in_basket()
