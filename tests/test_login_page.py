import allure
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import re

from tools.allure_tools.epics import AllureEpic
from tools.allure_tools.stories import AllureStories
from tools.allure_tools.features import AllureFeature
from allure_commons.types import Severity
from config import settings
from tools.routes import AppRoute
from test_data.models.login import LoginNegativeCase

@pytest.mark.regression
@pytest.mark.authorization

@allure.epic(AllureEpic.AUTHORIZATION)
@allure.feature(AllureFeature.LOGIN)
class TestAuthorization:


    @allure.story(AllureStories.INVALID_LOGIN)
    @allure.severity(Severity.CRITICAL)
    def test_invalid_login(self, login_page: LoginPage, invalid_login_case: LoginNegativeCase):
        case = invalid_login_case

        allure.dynamic.title(f"Login validation: {case.id}")
        login_page.open(AppRoute.LOGIN)
        login_page.fill_login_form(username=case.username, password=case.password)
        login_page.click_login_button()
        login_page.check_url_not_contain_pattern(re.compile(f'.*{AppRoute.PRODUCTS.value}'))
        login_page.check_login_error_alert(epic_sadface=case.epic_sadface)

    @allure.title('Login with valid username and password')
    @allure.story(AllureStories.SUCCESSFUL_LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self, login_page: LoginPage, products_page: ProductsPage):
        login_page.open(AppRoute.LOGIN)
        login_page.fill_login_form(username=settings.test_user.username, password=settings.test_user.password)
        login_page.click_login_button()
        login_page.check_current_url(re.compile(f'.*{AppRoute.PRODUCTS.value}'))
        products_page.check_visible_products_page()

    @allure.title("Logout")
    @allure.story(AllureStories.SUCCESSFUL_LOGOUT)
    @allure.severity(Severity.CRITICAL)
    def test_logout(self, login_page: LoginPage, products_page: ProductsPage):
        login_page.open(AppRoute.LOGIN)
        login_page.fill_login_form(settings.test_user.username, settings.test_user.password)
        login_page.click_login_button()
        products_page.navbar.open_menu()
        products_page.navbar.logout()
        login_page.check_visible_login_page()



