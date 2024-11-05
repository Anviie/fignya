import psycopg2
import environ

env = environ.Env()
environ.Env.read_env()

# Параметры подключения
conn_params = {
    'dbname': env('NAME'),
    'user': env('USER'),
    'password': env('PASSWORD'),
    'host': env('HOST'),
    'port': env('PORT')
}

try:
    # Подключение к базе данных
    conn = psycopg2.connect(**conn_params)
    print("Подключение успешно!")
except Exception as e:
    print(f"Ошибка подключения: {e}")
finally:
    # Закрытие соединения
    if conn:
        conn.close()