import mariadb


def main():
    conn = mariadb.connect(
        user='admindb',
        password='kiwi',
        # host='192.168.86.29',
        host='192.168.86.37',
        port=3306,
        database='PyFi'
    )
    cur = conn.cursor()

    cur.execute(
        "SELECT Times FROM SpeedTests;"
    )


    # cur.execute(
    #     "INSERT INTO SpeedTests (Location, Times, Ping, Down, Upload) "
    #     "VALUES (?, ?, ?, ?, ?)", ('lancer arms', '2019-01-01 12:01:00', 3, 4, 8)
    # )
    conn.commit()
    for (Location) in cur:
        print(f"Location: {Location}\nPing: ")


if __name__ == '__main__':
    main()
