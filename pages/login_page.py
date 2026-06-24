from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page
import allure

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._username_input = Input(page, '[data-test="username"]', 'username')
        self._password_input = Input(page, '[data-test="password"]', 'password')
        self._login_button = Button(page, '[data-test="login-button"]', 'login button')
        self._login_error_alert = Text(page, '[data-test="error"]', 'login error alert')

    @allure.step('Fill login form')
    def fill_login_form(self, username: str, password: str):
        self._username_input.fill(username)
        self._username_input.check_have_value(username)

        self._password_input.fill(password)
        self._password_input.check_have_value(password)

    def click_login_button(self):
        self._login_button.click()

    @allure.step('Check login error alert')
    def check_login_error_alert(self, epic_sadface):
        self._login_error_alert.check_visible()
        self._login_error_alert.check_have_text(epic_sadface)




    

