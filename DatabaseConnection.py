import mariadb
import pandas as pd


class DB:

    """
    initiates connection to database
    self.conn is the connection to the database
    self.cursor is the actions that will be performed in the database
    NOTE: After cursor performs an action, the results will be stored in cursor
    """
    def __init__(self):
        self.conn = mariadb.connect(
            user='snake',
            password='kiwi',
            # host='192.168.86.37',
            # this is the zero tier ip
            host='10.147.17.9',
            port=3306,
            database='PyFi'
        )
        self.cursor = self.conn.cursor(buffered=True)

    """
    used to pull data from the SpeedTests table
    If wanting to pull more than 1 col, separate by comma when calling extract
    If wanting all columns, enter '*'
    NOTE: Currently only works when extracting all data or from all columns
    """
    def extract(self, cols):
        self.cursor.execute(
            f"SELECT {cols} FROM SpeedTests;"
        )
        self.conn.commit()
        local = []
        time = []
        ping = []
        down = []
        up = []
        for (Location, Times, Ping, Download, Upload) in self.cursor:
            local.append(Location)
            time.append(Times)
            ping.append(Ping)
            down.append(Download)
            up.append(Upload)

        return pd.DataFrame(
            {
                'Location': local,
                'Times': time,
                'Ping': ping,
                'Download': down,
                'Upload': up
            },
        )

    def point(self, cols):
        self.cursor.execute(
            f"SELECT {cols} "
            f"FROM SpeedTests"
            f"WHERE Time >= (current_timestamp - '02')"  # find how to subtract 2 hours
            f"LIMIT 5;"  # get the top 5 results
        )
        self.conn.commit()
        local = []
        time = []
        ping = []
        down = []
        up = []
        for (Location, Times, Ping, Download, Upload) in self.cursor:
            local.append(Location)
            time.append(Times)
            ping.append(Ping)
            down.append(Download)
            up.append(Upload)

        return pd.DataFrame(
            {
                'Location': local,
                'Times': time,
                'Ping': ping,
                'Download': down,
                'Upload': up
            },
        )

    """
    preq: json (dictionary || list of dictionaries)
    Enters data into the database
    NOTE: Will likely need editing when actual json objects are passed in
    """
    def enter_data(self, data):
        location = data['Location']
        ping = data['Ping']
        down = data['Download']
        up = data['Upload']
        self.cursor.execute("INSERT INTO SpeedTests (Location, Ping, Download, Upload) "
                            "VALUES (?, ?, ?, ?)", (location, ping, down, up))
        self.conn.commit()
