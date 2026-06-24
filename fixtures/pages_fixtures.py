from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.item_page import ItemPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)

@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    return ProductsPage(page=page)

@pytest.fixture
def products_page_with_state(page_with_state: Page) -> ProductsPage:
    return ProductsPage(page=page_with_state)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page=page)

@pytest.fixture
def cart_page_with_state(page_with_state: Page) -> CartPage:
    return CartPage(page=page_with_state)

@pytest.fixture
def checkout_info_page(page: Page) -> CheckoutInfoPage:
    return CheckoutInfoPage(page=page)

@pytest.fixture
def checkout_info_page_with_state(page_with_state: Page) -> CheckoutInfoPage:
    return CheckoutInfoPage(page=page_with_state)


@pytest.fixture
def checkout_complete_page(page: Page) -> CheckoutCompletePage:
    return CheckoutCompletePage(page=page)

@pytest.fixture
def checkout_complete_page_with_state(page_with_state: Page) -> CheckoutCompletePage:
    return CheckoutCompletePage(page=page_with_state)

@pytest.fixture
def checkout_overview_page(page: Page) -> CheckoutOverviewPage:
    return CheckoutOverviewPage(page=page)

@pytest.fixture
def checkout_overview_page_with_state(page_with_state: Page) -> CheckoutOverviewPage:
    return CheckoutOverviewPage(page=page_with_state)

@pytest.fixture
def item_page(page: Page) -> ItemPage:
    return ItemPage(page=page)

@pytest.fixture
def item_page_with_state(page_with_state: Page) -> ItemPage:
    return ItemPage(page=page_with_state)