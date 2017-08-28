class LoginPageElements(object):
    def email_field(self):
        return self.driver.find_element_by_id("user-name-input")

    def password_field(self):
        return self.driver.find_element_by_id("password-input")

    def login_button(self):
        return self.driver.find_element_by_id("login-button")
