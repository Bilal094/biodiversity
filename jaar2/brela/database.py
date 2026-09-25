import psycopg2
from queries import *
from insert_data import *

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'admin'
DB_HOST = 'localhost'
DB_PORT = 5432

try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    

    cursor = conn.cursor()

    execute_queries(cursor)

    county_id = insert_county(cursor)

    conn.commit()
    print('Tabellen succesvol aangemaakt')


except psycopg2.Error as e:
    print(f'Er is een error opgetreden: {e}')