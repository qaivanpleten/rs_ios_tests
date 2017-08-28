class OrdersPageElements(object):
    def orders_button_in_router(self):
        return self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name=\" Orders\"]')

    def orders_page_title(self):
        return self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name=\"Orders\"]')
