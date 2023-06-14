import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

class Database():
    def __init__(self):
        self.connection = pymysql.connect(os.environ.get("MYSQL_HOST"),
                                          os.environ.get("MYSQL_USERNAME"),
                                          os.environ.get("MYSQL_PASSWORD"),
                                          os.environ.get("MYSQL_DATABASE"))
        self.cursor = self.connection.cursor()
    def init(self):
        """Create tables if they don't exist"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,
                               name VARCHAR(255), email VARCHAR(255),
                               password VARCHAR(255), is_active BOOLEAN, 
                               is_superuser BOOLEAN, money FLOAT, 
                               created_at DATETIME, updated_at DATETIME)""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS
                               weapons (id INT AUTO_INCREMENT PRIMARY KEY,
                               name VARCHAR(255), description VARCHAR(255),
                               power INT, price FLOAT, created_at DATETIME,
                               updated_at DATETIME)""")

    def teardown(self):
        """Drop tables"""
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.cursor.execute("DROP TABLE IF EXISTS weapons")

db = Database()


        