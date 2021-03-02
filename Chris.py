from titoooooooooo import DB




"""
Driver for creating the database, showing rows, and editing it
"""
def main():
    print("DBAPI Lab starting up...")
    print()
    db = DB()
    db.create_db()
    db.insert_base_data()

if __name__ == '__main__':
    main()
