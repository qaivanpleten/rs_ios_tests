from repspark_at.actions.actions_login_page import *
from repspark_at.elements.elements_orders_page import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class OrdersPage(BasePage):
    def open_orders_page(self):
        LoginPage(self.driver).login_full_case()
        OrdersPageElements(self.driver).orders_button_in_router().click()
        assert OrdersPageElements(self.driver).orders_page_title().is_displayed(), "Orders page title isn't displayed"
