import psycopg2
from create_tabels import *
from insert_data import *

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'admin'
DB_HOST = 'localhost'
DB_PORT = 5432

def connect_to_db():
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)

        cursor = conn.cursor()

        return conn, cursor

    except psycopg2.Error as e:
        print(f'Er is een error opgetreden: {e}')


conn, cursor = connect_to_db()

try:
    execute_queries(cursor)
    print('Tabellen succesvol aangemaakt')

except psycopg2.Error as e:
    print(f'Er is een error opgetreden bij het aanmaken van de tabellen: {e}')
    conn.rollback()

try:
    insert_all(cursor)
    conn.commit()
    print('Data succesvol ingevoerd')
except psycopg2.Error as e:
    print(f'Er is een error opgetreden bij het invoeren van data: {e}')
    conn.rollback()

