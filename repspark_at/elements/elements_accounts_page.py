class AccountsPageElements:
    def __init__(self, driver):
        self.driver = driver

    def accounts_page_in_router(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\" Accounts\"]")

    def accounts_page_title(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"Accounts\"]")

    def near_you_title(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"Located near you\"]")

    def near_you_icon(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"\"]")

    def account_name(self, acc_name):
        return self.driver.find_element_by_xpath(acc_name)

    # popup - allow or not to use geo location service
    def allow_button(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Allow\"]")

    def dont_allow_button(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Don’t Allow\"]")

    def accept_button(self):
        return self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"repspark\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther")
