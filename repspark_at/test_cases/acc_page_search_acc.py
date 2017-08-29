import time
import unittest

from repspark_at.actions.actions_accounts_page import *
from repspark_at.actions.setup_class import SetUpClass


class SearchAccount(SetUpClass):
    def test_1_open_acc_page(self):
        AccountsPage.open_account_details_page(self)
        try:
            AccountsPage.allow_to_use_location(self)
        except:
            pass
        time.sleep(5)
        AccountsPage.check_title(self)

    def test_2_search_account(self):
        AccountsPage.search_accounts_by_name(self, "Nike")

    def test_3_reset_search(self):
        AccountsPage.clear_search_input(self)


if __name__ == '__main__':
    unittest.main()
#
#
# # version 1
#
# class SearchAccount(SetUpClass):
#     def test_search_acc_by_name(self):
#         AccountsPage.open_account_details_page(self)
#         try:
#             AccountsPage.allow_to_use_location(self)
#         except:
#             pass
#         time.sleep(5)
#         AccountsPage.check_title(self)
#
#         AccountsPage.search_accounts_by_name(self, "Nike")
#
#
#
# class ResetSearch(SetUpClass):
#     def test_reset_search(self):
#         AccountsPage.open_account_details_page(self)
#         try:
#             AccountsPage.allow_to_use_location(self)
#         except:
#             pass
#         time.sleep(5)
#         AccountsPage.check_title(self)
#
#         AccountsPage.search_accounts_by_name(self, "Nike")
#
#         AccountsPage.clear_search_input(self)
#
# if __name__ == '__main__':
#     unittest.main()

# version 2

# class SearchAccount(SetUpClass):
#     def test_search_acc_by_name(self):
#         AccountsPage.open_account_details_page(self)
#         try:
#             AccountsPage.allow_to_use_location(self)
#         except:
#             pass
#         time.sleep(5)
#         AccountsPage.check_title(self)
#
#         AccountsPage.search_accounts_by_name(self, "Nike")
#
#
# class ResetSearch(SetUpClass):
#     def test_reset_search(self):
#         SearchAccount.test_search_acc_by_name(self)
#
#         AccountsPage.clear_search_input(self)
#
# if __name__ == '__main__':
#     unittest.main()
