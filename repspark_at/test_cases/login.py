import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class AppLogin(SetUpClass):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.set_user_name("qwerty@gmail.com")
        login_page.set_password("root")
        login_page.click_login_button()

        assert BrowsePage(self.driver).opened(), "Browse page title isn't opened"


if __name__ == '__main__':
    unittest.main()
