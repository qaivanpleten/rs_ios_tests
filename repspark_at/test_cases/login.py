import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class AppLogin(SetUpClass):
    def test_login(self):
        LoginPage.set_user_name(self, "qwerty@mail.com")
        LoginPage.set_password(self, "root")
        LoginPage.click_login_button(self)

        BrowsePage.check_title(self)


if __name__ == '__main__':
    unittest.main()
