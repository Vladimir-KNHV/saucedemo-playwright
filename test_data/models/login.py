from pydantic import BaseModel


class LoginNegativeCase(BaseModel):
    id: str
    username: str
    password: str
    epic_sadface: str