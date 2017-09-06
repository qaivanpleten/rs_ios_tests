import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class AddProductToCart(SetUpClass):
    def test_add_prod(self):
        LoginPage(self.driver).login_full_case()
        BrowsePage(self.driver).tap_on_add_to_cart_button()


if __name__ == '__main__':
    unittest.main()
