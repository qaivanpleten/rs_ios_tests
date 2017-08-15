import unittest

from repspark_at.actions.actions_login_page import *
from appium import webdriver

from repspark_at.actions.actions_browse_page import *


class repspark_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "IPhone Simulator"
        caps["app"] = "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    def test_login(self):
        LoginPage.set_user_name(self, "qwerty@mail.com")
        LoginPage.set_password(self, "root")
        LoginPage.click_login_button(self)

        BrowsePage.check_title(self)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

