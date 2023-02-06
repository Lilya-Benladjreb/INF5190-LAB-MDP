import sqlite3

class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/user.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def create_user(self, last_name, first_name, email, inscription_date, salt, hashed_password):
        connection = self.get_connection()
        connection.execute(("insert into users(nom, prenom, courriel, inscription, salt, hash)"
                            " values(?, ?, ?, ?)"), (last_name, first_name, email, inscription_date,
                                                     email, inscription_date, salt, hashed_password))
        connection.commit()    