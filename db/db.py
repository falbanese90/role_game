import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

class Database():
    def __init__(self):
        """Connect to database"""
        self.connection = pymysql.connect(os.environ.get("MYSQL_HOST"),
                                          os.environ.get("MYSQL_USERNAME"),
                                          os.environ.get("MYSQL_PASSWORD"),
                                          os.environ.get("MYSQL_DATABASE"))
        self.cursor = self.connection.cursor()
    def init(self):
        """Create tables if they don't exist"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                               (id SERIAL PRIMARY KEY,
                               name VARCHAR(255) NOT NULL, 
                               email VARCHAR(255) NOT NULL,
                               password VARCHAR(255) NOT NULL, 
                               is_active BOOLEAN, 
                               is_superuser BOOLEAN, 
                               money FLOAT, 
                               created_at DATETIME, 
                               updated_at DATETIME)""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS
                               weapons (id SERIAL PRIMARY KEY,
                               name VARCHAR(255) NOT NULL, 
                               description VARCHAR(255) NOT NULL,
                               power INT NOT NULL, 
                               price FLOAT NOT NULL, 
                               created_at DATETIME,
                               updated_at DATETIME)""")

    def teardown(self):
        """Drop tables"""
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.cursor.execute("DROP TABLE IF EXISTS weapons")

db = Database()


        