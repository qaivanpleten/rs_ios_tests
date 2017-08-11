import unittest
from appium import webdriver
from actions.actions_browse_page import *
from actions.actions_login_page import *


class search_product(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "IPhone Simulator"
        caps["app"] = "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    def test_1_search_product_by_id(self):
        LoginPage.login_full_case(self)
        BrowsePage.search_product_by_id(self, "201_5")

    def test_2_reset_search(self):
        BrowsePage.clear_search_input(self)
        #time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

