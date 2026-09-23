import psycopg2
from queries import create_county

DB_NAME = 'biodiversity'
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

    create_county_table = create_county()

    cursor.execute(create_county_table)
    conn.commit()
except psycopg2.Error as e:
    print(f'Er is een error opgetreden: {e}')