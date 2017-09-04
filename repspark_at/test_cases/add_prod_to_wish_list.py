import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class AddToWishListTesting(SetUpClass):
    def test_add_prod_to_wish_list(self):
        LoginPage.login_full_case(self)
        BrowsePage.add_to_wish_list_button(self)

        time.sleep(6)
        self.assertTrue(self.driver.find_element_by_id("star-1-added").is_displayed())


class DeleteFromWishList(SetUpClass):
    def test_delete_from_wish_list(self):
        AddToWishListTesting.test_add_prod_to_wish_list(self)
        BrowsePage.remove_from_wish_list_button(self)
        time.sleep(6)

        self.assertTrue(self.driver.find_element_by_id("star-1-removed").is_displayed())


if __name__ == '__main__':
    unittest.main()
