from .db import db
from models.structs import Weapon


cursor = db.cursor

class Weapons(Weapon, db=db):
    super().__init__(db=db)

    def add_weapon(self, name, description, power, price):
        cursor.execute("""INSERT INTO weapons 
                          (name, description, power, price) 
                          VALUES (%s, %s, %s, %s)""", 
                          (name, description, power, price))
        db.connection.commit()
        return 'Weapon added'
    
    def get_weapons(self):
        cursor.execute("SELECT * FROM weapons")
        return cursor.fetchall()
        
    
