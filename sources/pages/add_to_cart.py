from sources.generic_utilities.generic_methods import GenericMethods
from sources.utilities import custom_logger as cl
import  logging

class AddToCart(GenericMethods):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_add_to_cart(self):
        self.switch_to_child_window(self.driver)
        self.elementClick("add-to-cart-button")
        self.timeSleep(3)
