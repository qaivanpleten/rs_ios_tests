import unittest
import HtmlTestRunner

from test_cases.acc_page_search_acc import search_accounts
from test_cases.add_prod_to_wish_list import add_to_wish_list_and_delete_from_one
from test_cases.browse_page_search_prod import search_product
from test_cases.login import repspark_login
from test_cases.allow_to_use_geo_location_service import check_acc_page_after_allowing_to_use_location_service

# get all tests

login_test = unittest.TestLoader().loadTestsFromTestCase(repspark_login)
search_product_test = unittest.TestLoader().loadTestsFromTestCase(search_product)
add_prod_to_wish_list_test = unittest.TestLoader().loadTestsFromTestCase(add_to_wish_list_and_delete_from_one)
search_accounts_test = unittest.TestLoader().loadTestsFromTestCase(search_accounts)
check_acc_page_with_near_you_list_test = unittest.TestLoader().\
    loadTestsFromTestCase(check_acc_page_after_allowing_to_use_location_service)


suite = unittest.TestSuite((login_test, search_product_test, add_prod_to_wish_list_test, search_accounts_test,
                            check_acc_page_with_near_you_list_test))
#unittest.TextTestRunner(verbosity=2).run(suite)

# open the report file
outfile = open('/Users/user/PycharmProjects/repspark/reports/repspark_reports/SeleniumPythonTestsSummary.html', 'w')

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output='repspark_reports')

# run the suite using HTMLTestRunner
runner.run(suite)


