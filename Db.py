import sqlite3

class Database():
    def connect_db(self):
        self.conn = sqlite3.connect('clients.db')
        self.cursor = self.conn.cursor()

    def disconnect_db(self):
        self.conn.close(); print('disconnecting db')

    def makeTables(self):
        self.connect_db(); print('Connecting to db')
        # create table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients(
                code INTEGER PRIMARY KEY,
                name_client CHAR(80) NOT NULL,
                telephone INTEGER(20) NOT NULL,
                city CHAR(80)
            )''')

        self.conn.commit(); print('Created db')
        self.disconnect_db(); print('db disconnected')
