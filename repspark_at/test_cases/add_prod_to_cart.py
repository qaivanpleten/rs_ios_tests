import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class AddProductToCart(SetUpClass):
    def test_add_prod(self):
        LoginPage.login_full_case(self)

        BrowsePage.tap_on_add_to_cart_button(self)


if __name__ == '__main__':
    unittest.main()
