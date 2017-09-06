from selenium.common.exceptions import NoSuchElementException


class BrowsePageElements:
    def __init__(self, driver):
        self.driver = driver

    def browse_page_title(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"Browse\"]")

    def search_input(self):
        return self.driver.find_element_by_id("search-input")

    def product_id_string(self, id_path):
        return self.driver.find_element_by_xpath(id_path)

    def product_name_string(self, name_path):
        return self.driver.find_element_by_xpath(name_path)

    def reset_search_button(self):
        return self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name=\"clear-button\"]')

    def star_button_disabled(self):
        for n in range(3):
            try:
                return self.driver.find_element_by_id("star-" + str(n) + "-removed")

            except NoSuchElementException:
                continue

        raise Exception("There aren't any disabled star-buttons")

    def star_button_enabled(self):
        return self.driver.find_element_by_id("star-1-added")

    def firs_element_to_scroll(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"Pant_000\"]")

    def second_element_to_scroll(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"Pant_003\"]")

    def cart_button(self):
        return self.driver.find_element_by_xpath("//XCUIElementTypeOther[@name=\"\"]")

    def add_to_cart_button(self, product_number):
        return self.driver.find_element_by_xpath('(//XCUIElementTypeOther[@name=\"\"])[' + str(product_number) + ']')
