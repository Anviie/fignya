import psycopg2
from psycopg2 import OperationalError

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host="2.59.161.29",
            database="Anvie",
            user="Anvie",
            password="4819"
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Проверка подключения
conn = create_connection()