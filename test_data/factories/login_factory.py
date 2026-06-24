from test_data.models.login import LoginNegativeCase
from test_data.factories.fake_data import generate_username,generate_password

class LoginFactory:

    @staticmethod
    def unregistered_user():
        return LoginNegativeCase(
            id="unregistered_user",
            username=generate_username(),
            password=generate_password(),
            epic_sadface="Epic sadface: Username and password do not match any user in this service"
        )

    @staticmethod
    def empty_username_valid_password():
        return LoginNegativeCase(
            id="empty_username_valid_password",
            username="",
            password="secret_sauce",
            epic_sadface="Epic sadface: Username is required"
        )

    @staticmethod
    def valid_username_empty_password():
        return LoginNegativeCase(
            id="valid_username_empty_password",
            username="standard_user",
            password="",
            epic_sadface="Epic sadface: Password is required"
        )

    @staticmethod
    def empty_username_empty_password():
        return LoginNegativeCase(
            id="empty_username_empty_password",
            username="",
            password="",
            epic_sadface="Epic sadface: Username is required"
        )

    @staticmethod
    def unregistered_username_registered_password():
        return LoginNegativeCase(
            id="unregistered_username_registered_password",
            username=generate_username(),
            password="secret_sauce",
            epic_sadface="Epic sadface: Username and password do not match any user in this service"
        )

    @staticmethod
    def registered_username_unregistered_password():
        return LoginNegativeCase(
            id="registered_username_unregistered_password",
            username="standard_user",
            password=generate_password(),
            epic_sadface="Epic sadface: Username and password do not match any user in this service"
        )


