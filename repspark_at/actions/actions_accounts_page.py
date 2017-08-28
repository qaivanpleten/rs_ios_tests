from selenium.webdriver.common.keys import Keys

from repspark_at.actions.actions_login_page import *
from repspark_at.elements.elements_accounts_page import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class AccountsPage(BasePage):
    def open_acc_page(self):
        acc_button = AccountsPageElements.accounts_page_in_router(self)
        acc_button.click()

    def check_title(self):
        acc_title = AccountsPageElements.accounts_page_title(self)
        self.assertTrue(acc_title.is_displayed())

    def search_accounts_by_name(self, acc_name):
        search_input = BrowsePageElements.search_input(self)
        self.assertTrue(search_input.is_displayed())
        search_input.click()
        search_input.clear()
        search_input.send_keys(acc_name)
        search_input.send_keys(Keys.RETURN)

        # check product's ID (first product in the list)
        self.assertTrue(AccountsPageElements.account_name(self, '//XCUIElementTypeStaticText[@name=\"'
                                                          + acc_name + '\"]'))

    def clear_search_input(self):
        reset_search_button = BrowsePageElements.reset_search_button(self)
        reset_search_button.click()
        self.assertTrue(AccountsPageElements.accounts_page_title(self))

    def open_account_details_page(self):
        LoginPage.login_full_case(self)
        AccountsPage.open_acc_page(self)

    def allow_to_use_location(self):
        AccountsPageElements.allow_button(self).click()

    def dont_allow_to_use_location(self):
        AccountsPageElements.dont_allow_button(self).click()

    def accept_location_modal(self):
        AccountsPageElements.accept_button(self).click()
