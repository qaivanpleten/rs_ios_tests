import unittest

import HtmlTestRunner

from repspark_at.test_cases.acc_page_search_acc import SearchAccount
from repspark_at.test_cases.add_prod_to_wish_list import WishListTesting
from repspark_at.test_cases.allow_to_use_geo_location_service import \
    CheckAccPageAllowToUseLocation
from repspark_at.test_cases.browse_page_search_prod import SearchProduct
from repspark_at.test_cases.login import AppLogin

# get all tests

login_test = unittest.TestLoader().loadTestsFromTestCase(AppLogin)
search_product_test = unittest.TestLoader().loadTestsFromTestCase(SearchProduct)
add_prod_to_wish_list_test = unittest.TestLoader().loadTestsFromTestCase(WishListTesting)
search_accounts_test = unittest.TestLoader().loadTestsFromTestCase(SearchAccount)
check_acc_page_with_near_you_list_test = unittest.TestLoader(). \
    loadTestsFromTestCase(CheckAccPageAllowToUseLocation)

suite = unittest.TestSuite((login_test, search_product_test, add_prod_to_wish_list_test, search_accounts_test,
                            check_acc_page_with_near_you_list_test))
# unittest.TextTestRunner(verbosity=2).run(suite)

# open the report file
# outfile = open('/Users/user/PycharmProjects/repspark/reports/repspark_reports/SeleniumPythonTestsSummary.html', 'w')

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output='repspark_reports')

# run the suite using HTMLTestRunner
runner.run(suite)
