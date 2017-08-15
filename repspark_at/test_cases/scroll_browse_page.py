import unittest

from repspark_at.actions.actions_login_page import *
from appium import webdriver

from repspark_at.actions.actions_browse_page import *


class scroll_browser_page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "IPhone Simulator"
        caps["app"] = "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    def test_1_scroll_page(self):
        LoginPage.login_full_case(self)
        time.sleep(6)

        BrowsePage.swipe(self, '125', '119', '125', '572')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()