import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class SearchProduct(SetUpClass):
    def test_search_product_by_id(self):
        LoginPage.login_full_case(self)
        BrowsePage.search_product_by_id(self, "201_5")


class ResetSearchProduct(SetUpClass):
    def test_reset_search(self):
        SearchProduct.test_search_product_by_id(self)
        BrowsePage.clear_search_input(self)


if __name__ == '__main__':
    unittest.main()
