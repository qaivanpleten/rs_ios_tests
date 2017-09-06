import time

from selenium.webdriver.common.keys import Keys

from repspark_at.actions.actions_login_page import *
from repspark_at.mobile_functions.touch_actions import TouchAction


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class BrowsePage(BasePage):
    def opened(self):
        return BrowsePageElements(self.driver).browse_page_title().is_displayed()

    def check_title(self):
        browse_title = BrowsePageElements(self.driver).browse_page_title()
        assert browse_title.is_displayed(), "Browse page title isn't displayed"

    def search_product_by_id(self, product_id):
        search_input = BrowsePageElements(self.driver).search_input()

        assert search_input.is_displayed(), "Search input field isn't displayed"
        search_input.click()
        search_input.clear()
        search_input.send_keys(product_id)
        search_input.send_keys(Keys.RETURN)

        # check product's ID (first product in the list)
        assert (BrowsePageElements(self.driver).product_id_string('//XCUIElementTypeStaticText[@name=\"'
                                                                  + product_id + '\"]')).is_displayed, \
            "Product isn't found. Product title isn't displayed"

        # check product's NAME (first one in the list)
        assert (
            BrowsePageElements(self.driver).product_name_string(
                '//XCUIElementTypeStaticText[@name=\"Pant_005\"]')).is_displayed, \

            "First product isn't displayed"

    def clear_search_input(self):
        reset_search_button = BrowsePageElements(self.driver).reset_search_button()
        reset_search_button.click()

        # check product's ID (first product in the list)
        assert (
            BrowsePageElements(self.driver).product_id_string(
                '//XCUIElementTypeStaticText[@name=\"201_0\"]')).is_displayed, \
            "Product isn't displayed"

        # check product's NAME (first one in the list)
        assert (
            BrowsePageElements(self.driver).product_name_string(
                '//XCUIElementTypeStaticText[@name=\"Pant_000\"]')).is_displayed, \
            "Product isn't displayed"

    def add_to_wish_list_button(self):
        star_button = BrowsePageElements(self.driver).star_button_disabled()
        assert star_button.is_displayed(), "Star button isn't displayed"
        star_button.click()

    def remove_from_wish_list_button(self):
        star_button = BrowsePageElements(self.driver).star_button_enabled()
        assert star_button.is_displayed(), "Star button isn't displayed"
        star_button.click()

    def open_cart(self):
        LoginPage(self.driver).login_full_case()
        assert (BrowsePageElements(self.driver).cart_button()).is_displayed(), "Cart button isn't displayed"
        BrowsePageElements(self.driver).cart_button().click()
        time.sleep(5)

    def tap_on_add_to_cart_button(self):
        BrowsePageElements(self.driver).add_to_cart_button(2).click()


class Swipe(TouchAction):
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y)
        action.wait(ms=duration)
        action.move_to(x=end_x, y=end_y)
        action.release()
        action.perform()

        #return self
