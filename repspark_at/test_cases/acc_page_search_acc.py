import time
import unittest

from repspark_at.actions.actions_accounts_page import *
from repspark_at.actions.setup_class import SetUpClass


class SearchAccount(SetUpClass):
    def test_search_acc_by_name(self):
        acc_page = AccountsPage(self.driver)
        acc_page.open_account_details_page()
        try:
            acc_page.allow_to_use_location()
        except:
            pass
        time.sleep(5)
        acc_page.check_title()

        acc_page.search_accounts_by_name("Nike")


class ResetSearchAccount(SetUpClass):
    def test_reset_search(self):
        SearchAccount.test_search_acc_by_name()
        AccountsPage(self.driver).clear_search_input()


if __name__ == '__main__':
    unittest.main()
