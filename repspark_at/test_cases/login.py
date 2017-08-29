import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class AppLogin(SetUpClass):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.set_user_name("qwerty@gmail.com")
        login_page.set_password("root")
        login_page.click_login_button()

        # LoginPage.set_user_name(self, "qwerty@mail.com")
        # LoginPage.set_password(self, "root")
        # LoginPage.click_login_button(self)

        BrowsePage.check_title(self)
        #BrowsePage(self.driver).check_title()

        #self.assertTrue(BrowsePage(self.driver).opened())


if __name__ == '__main__':
    unittest.main()
