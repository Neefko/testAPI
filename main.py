# Импортируем FastAPI — это фреймворк для создания API
from fastapi import FastAPI

# Это нужно для того, чтобы разрешить запросы к API из других источников (в нашем случае — из Tkinter)
from fastapi.middleware.cors import CORSMiddleware

# Импортируем sqlite3 для работы с базой данных
import sqlite3

# Создаём приложение FastAPI
app = FastAPI()

# Добавляем CORS middleware, чтобы разрешить запросы с любых адресов (на случай, если будет обращаться другой клиент)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" означает — разрешить всё (можно ограничить, если нужно)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем любые HTTP-методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешаем любые заголовки
)

# Путь к нашей SQLite базе
DB_PATH = "db"

# Эта функция открывает базу, читает данные из таблицы `items` и возвращает их в виде списка словарей
def get_data():
    conn = sqlite3.connect(DB_PATH)           # Подключаемся к базе данных
    cursor = conn.cursor()                    # Создаём курсор для выполнения SQL-запросов
    cursor.execute("SELECT id, name FROM items")  # Выполняем SQL-запрос (предполагаем, что есть таблица `items`)
    rows = cursor.fetchall()                  # Получаем все строки результата
    conn.close()                              # Закрываем соединение
    # Преобразуем строки в список словарей
    return [{"id": row[0], "name": row[1]} for row in rows]

# Этот обработчик сработает, когда клиент сделает GET-запрос по адресу /items
@app.get("/items")
def read_items():
    return get_data()  # Просто возвращаем результат функции get_data()