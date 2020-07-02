from sources.pages.home_page import HomePage
from sources.pages.add_to_cart import AddToCart
from sources.generic_utilities.generic_methods import GenericMethods
class Amazon(GenericMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def searchProduct(self, product_name):
        HomePage(self.driver).searchBox(product_name)

    def addToCart(self):
        AddToCart(self.driver).click_on_add_to_cart()