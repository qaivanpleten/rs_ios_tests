import time

from selenium.webdriver.common.keys import Keys

from repspark_at.actions.actions_login_page import *
from repspark_at.mobile_functions.touch_actions import TouchAction


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class BrowsePage(BasePage):
    def opened(self):
        return BrowsePageElements.browse_page_title(self).is_displayed()

    def check_title(self):
        browse_title = BrowsePageElements.browse_page_title(self)
        assert browse_title.is_displayed(), "Browse page title isn't displayed"

    def search_product_by_id(self, product_id):
        search_input = BrowsePageElements.search_input(self)
        assert search_input.is_displayed(), "Search input field isn't displayed"
        search_input.click()
        search_input.clear()
        search_input.send_keys(product_id)
        search_input.send_keys(Keys.RETURN)

        # check product's ID (first product in the list)
        assert (BrowsePageElements.product_id_string(self, '//XCUIElementTypeStaticText[@name=\"'
                                                     + product_id + '\"]')).is_displayed, \
            "Product isn't found. Product title isn't displayed"

        # check product's NAME (first one in the list)
        assert (
        BrowsePageElements.product_name_string(self, '//XCUIElementTypeStaticText[@name=\"Pant_005\"]')).is_displayed, \
            "First product isn't displayed"

    def clear_search_input(self):
        reset_search_button = BrowsePageElements.reset_search_button(self)
        reset_search_button.click()

        # check product's ID (first product in the list)
        assert (
        BrowsePageElements.product_id_string(self, '//XCUIElementTypeStaticText[@name=\"201_0\"]')).is_displayed, \
            "Product isn't displayed"

        # check product's NAME (first one in the list)
        assert (
        BrowsePageElements.product_name_string(self, '//XCUIElementTypeStaticText[@name=\"Pant_000\"]')).is_displayed, \
            "Product isn't displayed"

    def add_to_wish_list_button(self):
        star_button = BrowsePageElements.star_button_disabled(self)
        assert star_button.is_displayed(), "Star button isn't displayed"
        star_button.click()

    def remove_from_wish_list_button(self):
        star_button = BrowsePageElements.star_button_enabled(self)
        assert star_button.is_displayed(), "Star button isn't displayed"
        star_button.click()

    def open_cart(self):
        LoginPage.login_full_case(self)
        assert (BrowsePageElements.cart_button(self)).is_displayed(), "Cart button isn't displayed"
        (BrowsePageElements.cart_button(self)).click()
        time.sleep(5)

    def tap_on_add_to_cart_button(self):
        (BrowsePageElements.add_to_cart_button(self, 2)).click()


class Swipe(TouchAction):
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        action = TouchAction(self).press(x=start_x, y=start_y).wait(ms=duration).move_to(x=end_x, y=end_y).release()
        action.perform(self)

        return self
