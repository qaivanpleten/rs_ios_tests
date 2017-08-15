import time
import unittest

from appium import webdriver

from repspark_at.actions.actions_accounts_page import *


class search_accounts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "IPhone Simulator"
        caps["app"] = "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    def test_1_open_acc_page(self):
        AccountsPage.open_account_details_page(self)
        try:
            AccountsPage.allow_to_use_location(self)
        except:
            pass
        time.sleep(5)
        AccountsPage.check_title(self)

    def test_2_search_account(self):
        AccountsPage.search_accounts_by_name(self, "Nike")

    def test_3_reset_search(self):
        AccountsPage.clear_search_input(self)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

