import unittest, time
from appium import webdriver
from actions.actions_accounts_page import *
from elements.elements_accounts_page import *

class check_acc_page_after_allowing_to_use_location_service(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "IPhone Simulator"
        caps["app"] = "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    def test_check_the_page(self):
        LoginPage.login_full_case(self)
        AccountsPage.open_acc_page(self)
        try:
            AccountsPage.allow_to_use_location(self)
        except:
            pass

        AccountsPage.check_title(self)
        self.assertTrue(AccountsPageElements.near_you_title(self).is_displayed())
        self.assertTrue(AccountsPageElements.near_you_icon(self).is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

