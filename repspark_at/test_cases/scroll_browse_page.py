import unittest

from repspark_at.actions.actions_browse_page import *
from repspark_at.actions.setup_class import SetUpClass


class ScrollBrowserPage(SetUpClass):
    def test_1_scroll_page(self):
        LoginPage.login_full_case(self)
        time.sleep(6)

        Swipe.swipe(self, '125', '119', '125', '572')


if __name__ == '__main__':
    unittest.main()
