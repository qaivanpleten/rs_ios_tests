import unittest

from repspark_at.actions.actions_accounts_page import *
from repspark_at.actions.setup_class import SetUpClass


class CheckAccPageWithBannedLocation(SetUpClass):
    def test_check_the_page(self):
        LoginPage.login_full_case(self)
        AccountsPage.open_acc_page(self)
        try:
            AccountsPage.dont_allow_to_use_location(self)
            AccountsPage.accept_location_modal(self)
        except:
            try:
                AccountsPage.accept_location_modal(self)
            except:
                pass

        AccountsPage.check_title(self)


if __name__ == '__main__':
    unittest.main()
