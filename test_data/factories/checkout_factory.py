from test_data.models.checkout import CheckoutNegativeCase
from test_data.factories.fake_data import generate_username, generate_postal_code

class CheckoutFactory:

    @staticmethod
    def empty_form():
        return CheckoutNegativeCase(
            id='Empty form',
            first_name='',
            last_name='',
            postal_code='',
            epic_sadface='Error: First Name is required'
        )

    @staticmethod
    def empty_first_name():
        return CheckoutNegativeCase(
            id='Empty first name',
            first_name='',
            last_name=generate_username(),
            postal_code=generate_postal_code(),
            epic_sadface='Error: First Name is required'
        )

    @staticmethod
    def empty_last_name():
        return CheckoutNegativeCase(
            id='Empty last name',
            first_name=generate_username(),
            last_name='',
            postal_code=generate_postal_code(),
            epic_sadface='Error: Last Name is required'
        )

    @staticmethod
    def empty_postal_code():
        return CheckoutNegativeCase(
            id='Empty postal code',
            first_name=generate_username(),
            last_name=generate_username(),
            postal_code='',
            epic_sadface='Error: Postal Code is required'
        )