import unittest

from repspark_at.actions.actions_accounts_page import *
from repspark_at.actions.setup_class import SetUpClass
from repspark_at.elements.elements_accounts_page import *


class CheckAccPageAllowToUseLocation(SetUpClass):
    def test_check_the_page(self):
        LoginPage.login_full_case(self)
        AccountsPage.open_acc_page(self)
        try:
            AccountsPage.allow_to_use_location(self)
        except:
            pass

        AccountsPage.check_title(self)
        assert AccountsPageElements.near_you_title(self).is_displayed(), "Title 'Located near you' isn't displayed"
        assert AccountsPageElements.near_you_icon(self).is_displayed(), "'Near you' icon isn't displayed"


if __name__ == '__main__':
    unittest.main()
