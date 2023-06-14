from .db import db
from models.structs import User


cursor = db.cursor

class Users(User, db=db):
    super().__init__(db=db)

    def add_user(self, name, email, password, money):
        cursor.execute("""INSERT INTO users 
                          (name, email, password, money) 
                          VALUES (%s, %s, %s, %s)""", 
                          (name, email, password, money))
        db.connection.commit()
        return 'User added'
    
    def get_users(self):
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    