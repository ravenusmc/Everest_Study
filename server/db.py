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

    # This method will check to ensure that the username is in the database and then log them in.
    def verify_user(self, username, password):
        # Setting up a user dictionary
        user = {}
        # encoding the password to utf-8
        password = password.encode('utf-8')
        # Creating the query for the database
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        # Here I check to see if the username is in the database.
        if str(row) == 'None':
            login_flag = False
            not_found = True
            password_no_match = False
        # If the user name is in the database I move here to check if the password
        # is valid.
        else:
            hashed = row[5].encode('utf-8')
            if bcrypt.checkpw(password, hashed):
                user["id"] = row[0]
                user['username'] = row[1]
                login_flag = True
                not_found = False
                password_no_match = False
            # This is a final catch all area. Basically if the password does not match
            # the user is not getting in.
            else:
                login_flag = False
                not_found = False
                password_no_match = True
        return login_flag, not_found, password_no_match, user 
