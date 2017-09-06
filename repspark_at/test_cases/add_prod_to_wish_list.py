import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class AddToWishListTesting(SetUpClass):
    def test_add_prod_to_wish_list(self):
        LoginPage(self.driver).login_full_case()
        BrowsePage(self.driver).add_to_wish_list_button()

        time.sleep(6)
        assert self.driver.find_element_by_id(
            "star-1-added").is_displayed(), "Product wasn't added to wish list. Orange button isn't displayed"


class DeleteFromWishList(SetUpClass):
    def test_delete_from_wish_list(self):
        AddToWishListTesting.test_add_prod_to_wish_list(self)
        BrowsePage(self.driver).remove_from_wish_list_button()
        time.sleep(6)

        assert self.driver.find_element_by_id(
            "star-1-removed").is_displayed(), "Product wasn't deleted from wish list. Gray button isn't dispalayed"


if __name__ == '__main__':
    unittest.main()
