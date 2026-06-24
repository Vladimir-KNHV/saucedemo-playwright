from pydantic import BaseModel

class CheckoutNegativeCase(BaseModel):
    id: str
    first_name: str
    last_name: str
    postal_code: str
    epic_sadface: str