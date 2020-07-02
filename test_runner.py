from test_scripts.test_amazon import Amazon
from sources.utilities import excel
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class Test_Amazon():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.amazon = Amazon(self.driver)

    def test_tc_001_add_product(self):
        product_name = excel.get_value("Cart","TC_001","ProductName")
        self.amazon.searchProduct(product_name)
        self.amazon.addToCart()


 # pytest -h test_runner.py  C:/python_projects/amazon_fb/resources/reports/html_report/ap.html

# 1. iterators, generators, decorators
# 2.  oops, lambda , map, reduce, filters
# 3. file handling (json, pickle)
# 4. action chains
# 5. select class
# 6. window handles
# 7. iframes, alerts, pops, JS executor.
# 8. pytest (marker , fixtures)--> skip, skipif, parameterized, custom marker.
