from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Добавляем CORS middleware, чтобы разрешить запросы с любых адресов (на случай, если будет обращаться другой клиент)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # разрешить всё
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем любые HTTP-методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешаем любые заголовки
)

DB_PATH = "db"

# возвращает их в виде списка словарей
def get_data():
    conn = sqlite3.connect(DB_PATH)           # Подключаемся к базе данных
    cursor = conn.cursor()                    # Создаём курсор для выполнения SQL-запросов
    cursor.execute("SELECT id, name FROM items")  # Выполняем SQL-запрос (предполагаем, что есть таблица `items`)
    rows = cursor.fetchall()                  # Получаем все строки результата
    conn.close()                              # Закрываем соединение
    # Преобразуем строки в список словарей
    return [{"id": row[0], "name": row[1]} for row in rows]

@app.get("/items")
def read_items():
    return get_data()  # Просто возвращаем результат функции get_data()