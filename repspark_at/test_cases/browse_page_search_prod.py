import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class SearchProduct(SetUpClass):
    def test_1_search_product_by_id(self):
        LoginPage.login_full_case(self)
        BrowsePage.search_product_by_id(self, "201_5")

    def test_2_reset_search(self):
        BrowsePage.clear_search_input(self)
        # time.sleep(5)


if __name__ == '__main__':
    unittest.main()
