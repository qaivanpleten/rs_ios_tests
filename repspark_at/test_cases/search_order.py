import unittest

from repspark_at.actions.actions_orders_page import *
from repspark_at.actions.setup_class import SetUpClass


class SearchOrder(SetUpClass):
    def test_1_open_orders_page(self):
        OrdersPage(self.driver).open_orders_page()


if __name__ == '__main__':
    unittest.main()
