from selenium.webdriver.common.keys import Keys

from repspark_at.actions.actions_login_page import *
from repspark_at.elements.elements_accounts_page import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class AccountsPage(BasePage):
    def open_acc_page(self):
        acc_button = AccountsPageElements(self.driver).accounts_page_in_router()
        acc_button.click()

    def check_title(self):
        acc_title = AccountsPageElements(self.driver).accounts_page_title()
        assert acc_title.is_displayed(), "Account page title isn't displayed"

    def search_accounts_by_name(self, acc_name):
        search_input = BrowsePageElements(self.driver).search_input()
        assert search_input.is_displayed(), "Search field isn't displayed"
        search_input.click()
        search_input.clear()
        search_input.send_keys(acc_name)
        search_input.send_keys(Keys.RETURN)

        # check product's ID (first product in the list)
        assert (AccountsPageElements(self.driver).account_name('//XCUIElementTypeStaticText[@name=\"'

                                                  + acc_name + '\"]')).is_displayed(), \
            "ID of the first product in the list is wrong or thee isn't any product"

    def clear_search_input(self):
        reset_search_button = BrowsePageElements(self.driver).reset_search_button()
        reset_search_button.click()
        AccountsPage(self.driver).check_title()


    def open_account_details_page(self):
        LoginPage(self.driver).login_full_case()
        AccountsPage(self.driver).open_acc_page()

    def allow_to_use_location(self):
        AccountsPageElements(self.driver).allow_button().click()

    def dont_allow_to_use_location(self):
        AccountsPageElements(self.driver).dont_allow_button().click()

    def accept_location_modal(self):
        AccountsPageElements(self.driver).accept_button().click()
