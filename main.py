from db_helper import DatabaseFactory

if __name__ == '__main__':
    try:
        # Get MySQL connection
        mysql_db = DatabaseFactory.DatabaseFactory.create_database('mysql')
        mysql_connection = mysql_db.connect()
        print("Connected to MySQL")

        # Get PostgreSQL connection
        postgres_db = DatabaseFactory.DatabaseFactory.create_database('postgres')
        postgres_connection = postgres_db.connect()
        print("Connected to PostgreSQL")

    except Exception as e:
        print(f"Error: {e}")
