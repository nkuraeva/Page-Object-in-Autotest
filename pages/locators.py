from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(text(), 'View basket')]")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BTN_BASKET = (By.CSS_SELECTOR, ".btn-group,a.btn-default")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-main,h1")
    IN_BASKET_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-main,p.price_color")
    IN_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    ALERT = (By.CSS_SELECTOR, "div#content_inner p")