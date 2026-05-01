import psycopg2
import traceback


def connect():
    config = {
        "host": "localhost",
        "database": "phonebook",
        "user": "postgres",
        "password": "1234",
        "port": "5432"
    }

    print("CONFIG:", config)

    try:
        conn = psycopg2.connect(**config)
        print("Connected successfully")
        return conn
    except Exception:
        traceback.print_exc()
        return None
