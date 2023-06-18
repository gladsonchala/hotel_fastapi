import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('data.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        # Create the "users" table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                middle_name TEXT,
                gender TEXT NOT NULL,
                roles TEXT NOT NULL
            )
        ''')

        # Create the "photos" table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS photos (
                id TEXT PRIMARY KEY,
                url TEXT NOT NULL,
                caption TEXT
            )
        ''')

        # Create the "rooms" table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                room_id TEXT PRIMARY KEY,
                hotel_id TEXT,
                name TEXT,
                description TEXT,
                price REAL,
                beds INTEGER
            )
        ''')

        # Create the "hotels" table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hotels (
                hotel_id TEXT PRIMARY KEY,
                name TEXT,
                grounds TEXT,
                address TEXT,
                city TEXT,
                region TEXT,
                latitude REAL,
                longitude REAL,
                phone TEXT,
                email TEXT,
                website TEXT,
                description TEXT,
                stars INTEGER,
                price_range TEXT,
                services TEXT,
                map_url TEXT
            )
        ''')

        self.connection.commit()

    def close(self):
        self.connection.close()
