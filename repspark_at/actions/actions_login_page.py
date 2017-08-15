from repspark_at.elements.elements_login_page import *

from repspark_at.elements.elements_browse_page import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):

    def set_user_name(self, username):
        email_field = LoginPageElements.email_field(self)
        self.assertTrue(email_field.is_displayed())
        email_field.click()
        email_field.send_keys(username)

    def set_password(self, password):
        password_field = LoginPageElements.password_field(self)
        self.assertTrue(password_field.is_displayed())
        password_field.click()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = LoginPageElements.login_button(self)
        self.assertTrue(login_button.is_displayed())
        login_button.click()
        #time.sleep(5)

    def login_full_case(self):
        email_field = LoginPageElements.email_field(self)
        self.assertTrue(email_field.is_displayed())
        email_field.click()
        email_field.send_keys("johndoe@gmail.com")

        password_field = LoginPageElements.password_field(self)
        self.assertTrue(password_field.is_displayed())
        password_field.click()
        password_field.send_keys("root")

        login_button = LoginPageElements.login_button(self)
        self.assertTrue(login_button.is_displayed())
        login_button.click()

        self.assertTrue(BrowsePageElements.browse_page_title(self).is_displayed())

