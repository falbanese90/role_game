import pydantic
import datetime

class Weapon(pydantic.BaseModel):
    id: int | None
    name: str
    description: str
    power: int
    price: float
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __repr__(self):
        return f"<Weapon {self.name}>"

    class Config:
        orm_mode = True

class User(pydantic.BaseModel):
    id: int | None
    name: str
    email: str
    password: str
    is_active: None | bool
    is_superuser: bool | None
    weapons: list[Weapon] = []
    money: float
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __repr__(self):
        return f"<User {self.name}>"

    class Config:
        orm_mode = True