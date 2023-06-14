from .db import db
from models.structs import Weapon


cursor = db.cursor

class Weapon(Weapon, db=db):
    super().__init__(db=db)

    def add_weapon():
        cursor.execute("INSERT INTO weapons (name, description, power, price) VALUES (%s, %s, %s, %s)", (self.name, self.description, self.power, self.price))
