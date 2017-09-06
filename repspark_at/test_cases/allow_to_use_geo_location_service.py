import unittest

from repspark_at.actions.actions_accounts_page import *
from repspark_at.actions.setup_class import SetUpClass
from repspark_at.elements.elements_accounts_page import *


class CheckAccPageAllowToUseLocation(SetUpClass):
    def test_check_the_page(self):
        acc_page = AccountsPage(self.driver)

        LoginPage(self.driver).login_full_case()
        acc_page.open_acc_page()
        try:
            acc_page.allow_to_use_location()
        except:
            pass

        acc_page.check_title()
        assert AccountsPageElements(
            self.driver).near_you_title().is_displayed(), "Title 'Located near you' isn't displayed"
        assert AccountsPageElements(self.driver).near_you_icon().is_displayed(), "'Near you' icon isn't displayed"


if __name__ == '__main__':
    unittest.main()
