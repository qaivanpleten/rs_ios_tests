import unittest

from repspark_at.actions.actions_login_page import *
from appium import webdriver

from repspark_at.actions.actions_browse_page import *


class add_to_wish_list_and_delete_from_one(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "iOS"
        caps["platformVersion"] = "10.3"
        caps["deviceName"] = "IPhone Simulator"
        caps["app"] = "/Users/user/Desktop/RepSpark-App/ios/build/Build/Products/Debug-iphonesimulator/repspark.app"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    def test_add_prod_to_wish_list(self):
        LoginPage.login_full_case(self)
        BrowsePage.add_to_wish_list_button(self)

        time.sleep(6)
        self.assertTrue(self.driver.find_element_by_id("star-1-added").is_displayed())

    def test_delete_from_wish_list(self):
        BrowsePage.remove_from_wish_list_button(self)
        time.sleep(6)

        self.assertTrue(self.driver.find_element_by_id("star-1-removed").is_displayed())




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


