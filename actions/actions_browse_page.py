from selenium.webdriver.common.keys import Keys
import time
from actions.actions_login_page import *
from mobile_functions.touch_actions import TouchAction



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class BrowsePage(BasePage):
    def check_title(self):
        browse_title = BrowsePageElements.browse_page_title(self)
        self.assertTrue(browse_title.is_displayed())

    def search_product_by_id(self, product_id):
        search_input = BrowsePageElements.search_input(self)
        self.assertTrue(search_input.is_displayed())
        search_input.click()
        search_input.clear()
        search_input.send_keys(product_id)
        search_input.send_keys(Keys.RETURN)

        # check product's ID (first product in the list)
        self.assertTrue(BrowsePageElements.product_id_string(self, '//XCUIElementTypeStaticText[@name=\"'
                                                             + product_id + '\"]'))
        # check product's NAME (first one in the list)
        self.assertTrue(BrowsePageElements.product_name_string(self, '//XCUIElementTypeStaticText[@name=\"Pant_005\"]'))

    def clear_search_input(self):
        reset_search_button = BrowsePageElements.reset_search_button(self)
        reset_search_button.click()

        # check product's ID (first product in the list)
        self.assertTrue(BrowsePageElements.product_id_string(self, '//XCUIElementTypeStaticText[@name=\"201_0\"]'))

        # check product's NAME (first one in the list)
        self.assertTrue(BrowsePageElements.product_name_string(self, '//XCUIElementTypeStaticText[@name=\"Pant_000\"]'))

    def add_to_wish_list_button(self):
        star_button = BrowsePageElements.star_button_disabled(self)
        self.assertTrue(star_button.is_displayed())
        star_button.click()

    def remove_from_wish_list_button(self):
        star_button = BrowsePageElements.star_button_enabled(self)
        self.assertTrue(star_button.is_displayed())
        star_button.click()


    def open_cart(self):
        LoginPage.login_full_case(self)
        self.assertTrue((BrowsePageElements.cart_button(self)).is_displayed())
        (BrowsePageElements.cart_button(self)).click()
        time.sleep(5)

    def tap_on_add_to_cart_button(self):
        (BrowsePageElements.add_to_cart_button(self, 2)).click()

    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        action = TouchAction(self).press(x=start_x, y=start_y).wait(ms=duration).move_to(x=end_x, y=end_y).release()
        action.perform()

        return self