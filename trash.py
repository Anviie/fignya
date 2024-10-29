import psycopg2
from psycopg2 import OperationalError

def create_connection():
    connection = None
    try:
        # Замените параметры на свои
        connection = psycopg2.connect(
            host="2.59.161.29",  # IP-адрес вашего сервера
            database="Anvie",  # Имя вашей базы данных
            user="Anvie",  # Имя пользователя
            password="4819"  # Пароль пользователя
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Проверка подключения
conn = create_connection()