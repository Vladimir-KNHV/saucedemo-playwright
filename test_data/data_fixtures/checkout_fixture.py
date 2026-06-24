import pytest
from test_data.factories.checkout_factory import CheckoutFactory
from test_data.models.checkout import CheckoutNegativeCase


@pytest.fixture(params=[
    CheckoutFactory.empty_form(),
    CheckoutFactory.empty_first_name(),
    CheckoutFactory.empty_last_name(),
    CheckoutFactory.empty_postal_code()
], ids=lambda x: x.id)
def invalid_checkout_case(request) -> CheckoutNegativeCase:
    case = request.param
    return case