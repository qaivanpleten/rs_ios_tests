import unittest

from repspark_at.actions.actions_accounts_page import *
from repspark_at.actions.setup_class import SetUpClass


class CheckAccPageWithBannedLocation(SetUpClass):
    def test_check_the_page(self):
        acc_page = AccountsPage(self.driver)

        LoginPage(self.driver).login_full_case()
        acc_page.open_acc_page()
        try:
            acc_page.dont_allow_to_use_location()
            acc_page.accept_location_modal()
        except:
            try:
                acc_page.accept_location_modal()
            except:
                pass

        acc_page.check_title()


if __name__ == '__main__':
    unittest.main()
