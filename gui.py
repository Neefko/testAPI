import tkinter as tk
import requests

API_URL = "http://127.0.0.1:8000/items"

def fetch_items():
    try:
        response = requests.get(API_URL)
        items = response.json()
        listbox.delete(0, tk.END)
        for item in items:
            listbox.insert(tk.END, f"{item['id']}: {item['name']}")
    except Exception as e:
        listbox.insert(tk.END, f"Ошибка: {e}")

root = tk.Tk()
root.title("Items Viewer")

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

button = tk.Button(root, text="Обновить", command=fetch_items)
button.pack()

root.mainloop()

