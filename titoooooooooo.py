import time
import os
import sqlite3


class DB:
    def __init__(self):
        self.db_name = "SpeedDatabase"
        file = os.path.join("data", self.db_name + ".db")
        self.db_file = os.path.abspath(file)

    def create_db(self):
        if os.path.exists(self.db_file):
            print("Database already exists at following location, skipping create")
            print(self.db_file)
            return

        print("Creating database file at: ")
        print(self.db_file)

        with sqlite3.connect(self.db_file) as db:
            db.execute(
                'create table Speeds ' +
                '(location text'
                'times datetime default current_timestamp,'
                'ping INTEGER,'
                'down REAL,'
                'upload REAL,'
                'PRIMARY KEY(location, times)'
                ');'

            )

        print('')

    def insert_base_data(self):
        print('')
        print('Inserting base data')

        if self.has_data():
            print("Data already inserted, skpping")
            return

        with sqlite3.connect(self.db_file) as db:
            db.execute(
                'INSERT INTO SpeedDatabase (location, ping, down, up) VALUES '
                '("point", null, 3, 4, 8)')
            time.sleep(.200)
        print("done")

    def has_data(self):
        with sqlite3.connect(self.db_file) as db:
            cursor = db.execute("SELECT count(*) FROM SpeedDatabase")
            data_count = cursor.fetchone()[0]
            return data_count > 0

    def show_all_rows(self):
        print("Showing all rows")
        with sqlite3.connect(self.db_file) as db:
            cursor = db.execute("SELECT * FROM SpeedDatabase")
            for row in cursor:
                print(row)
        print()
