from repspark_at.elements.elements_browse_page import *
from repspark_at.elements.elements_login_page import *

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    def set_user_name(self, username):
        email_field = LoginPageElements.email_field(self)
        assert email_field.is_displayed(), "email field isn't displayed"
        email_field.click()
        email_field.send_keys(username)

    def set_password(self, password):
        password_field = LoginPageElements.password_field(self)
        assert password_field.is_displayed(), "password field isn't displayed"
        password_field.click()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = LoginPageElements.login_button(self)
        assert login_button.is_displayed(), "login button isn't displayed"
        login_button.click()
        # time.sleep(5)

    def login_full_case(self):
        email_field = LoginPageElements.email_field(self)
        assert email_field.is_displayed(), "email field isn't displayed"

        email_field.click()
        email_field.send_keys("johndoe@gmail.com")

        password_field = LoginPageElements.password_field(self)
        assert password_field.is_displayed(), "password field isn't displayed"
        password_field.click()
        password_field.send_keys("root")

        login_button = LoginPageElements.login_button(self)
        assert login_button.is_displayed(), "login button isn't displayed"
        login_button.click()

        assert (BrowsePageElements.browse_page_title(self)).is_displayed(), "Browser page title isn't displayed"