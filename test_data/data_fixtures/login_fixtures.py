import pytest
from test_data.factories.login_factory import LoginFactory
from test_data.models.login import LoginNegativeCase

@pytest.fixture(params=[
    LoginFactory.unregistered_user(),
    LoginFactory.empty_username_valid_password(),
    LoginFactory.valid_username_empty_password(),
    LoginFactory.empty_username_empty_password(),
    LoginFactory.unregistered_username_registered_password(),
    LoginFactory.registered_username_unregistered_password()
], ids=lambda x: x.id)
def invalid_login_case(request) -> LoginNegativeCase:
    case = request.param
    return case