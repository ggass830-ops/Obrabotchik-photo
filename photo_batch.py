import tkinter as tk
from tkinter import filedialog, messagebox, ttk

FORMATS = ("JPEG", "PNG", "WEBP")


def choose():
    filedialog.askdirectory()


def run():
    messagebox.showinfo("Прототип")


root = tk.Tk()
root.title("Пакетный обработчик фото")
tk.Button(root, text="Выбрать папку", command=choose).grid(row=0, column=0, padx=10, pady=10, sticky="w")
info = tk.Label(root, text="Папка не выбрана")
info.grid(row=0, column=1, columnspan=3, sticky="w")
tk.Label(root, text="Ширина, px:").grid(row=1, column=0, sticky="e")
width = tk.Entry(root, width=8)
width.grid(row=1, column=1, sticky="w")
tk.Label(root, text="Формат:").grid(row=1, column=2, sticky="e")
fmt = ttk.Combobox(root, values=list(FORMATS), state="readonly", width=8)
fmt.current(0)
fmt.grid(row=1, column=3, padx=10)
tk.Label(root, text="Водяной знак:").grid(row=2, column=0, sticky="e", pady=6)
mark = tk.Entry(root, width=30)
mark.grid(row=2, column=1, columnspan=3, sticky="w")
tk.Button(root, text="Обработать", command=run).grid(row=3, column=0, padx=10, pady=6, sticky="w")
listbox = tk.Listbox(root, width=60, height=12)
listbox.grid(row=4, column=0, columnspan=4, padx=10, pady=(0, 10))
root.mainloop()
