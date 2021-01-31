from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
    
    def right_name_in_basket(self):
        product_name = self.find_element(*ProductPageLocators.PRODUCT_NAME).text
        in_basket_name = self.find_element(*ProductPageLocators.IN_BASKET_NAME).text
        assert product_name == in_basket_name, "Product name is not/wrong in basket"
        print(product_name, in_basket_name)

    def right_price_in_basket(self):
        product_price = self.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        in_basket_price = self.find_element(*ProductPageLocators.IN_BASKET_PRICE).text
        assert product_price == in_basket_price, "Price is not/wrong in basket"
        print(product_price, in_basket_price)