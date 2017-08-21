from repspark_at.actions.actions_login_page import *
from repspark_at.elements.elements_orders_page import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class OrdersPage(BasePage):
    def open_orders_page(self):
        LoginPage.login_full_case(self)
        OrdersPageElements.orders_button_in_router(self).click()
        self.assertTrue(OrdersPageElements.orders_page_title(self).is_displayed())
