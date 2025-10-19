# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime


class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='gus',
                                            password='pass',
                                            host='localhost',
                                            port=3306,
                                            database='everest_project')
        self.cursor = self.conn.cursor()

    def encrypt_pass(self, post_data):
        password = post_data['payload']['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed

  # This method will insert a new user into the database.
    def insert(self, post_data, hashed):
        self._SQL = """insert into users
                          (username, firstName, lastName, email, password)
                          values
                          (%s, %s, %s, %s, %s)"""
        self.cursor.execute(self._SQL, (post_data['payload']['username'], post_data['payload']['firstName'],
                                        post_data['payload']['lastName'], post_data['payload']['email'], hashed))
        self.conn.commit()
        user_created = True
        return user_created
