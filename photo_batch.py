import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps

EXT = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
folder, files = "", []


def choose():
    global folder, files
    d = filedialog.askdirectory()
    if not d:
        return
    folder = d
    files = [f for f in sorted(os.listdir(d)) if f.lower().endswith(EXT)]
    listbox.delete(0, "end")
    for f in files:
        listbox.insert("end", f)
    info.config(text=f"Найдено фото: {len(files)}")
    if not files:
        messagebox.showwarning("Ошибка", "В папке нет изображений")


def run():
    if not files:
        messagebox.showwarning("Ошибка", "Сначала выберите папку с фото")
        return
    w = width.get().strip()
    if w and not w.isdigit():
        messagebox.showwarning("Ошибка", "Ширина должна быть числом")
        return
    out = os.path.join(folder, "обработано")
    os.makedirs(out, exist_ok=True)
    listbox.delete(0, "end")
    ok = 0
    for f in files:
        try:
            img = ImageOps.exif_transpose(Image.open(os.path.join(folder, f)))
            if w:
                wpx = int(w)
                img = img.resize((wpx, max(1, round(img.height * wpx / img.width))))
            img.save(os.path.join(out, f))
            listbox.insert("end", "OK  " + f)
            ok += 1
        except Exception:
            listbox.insert("end", "ОШИБКА  " + f)
    info.config(text=f"Обработано: {ok} из {len(files)}")


root = tk.Tk()
root.title("Пакетный обработчик фото")
tk.Button(root, text="Выбрать папку", command=choose).grid(row=0, column=0, padx=10, pady=10, sticky="w")
info = tk.Label(root, text="Папка не выбрана")
info.grid(row=0, column=1, columnspan=2, sticky="w")
tk.Label(root, text="Ширина, px:").grid(row=1, column=0, sticky="e")
width = tk.Entry(root, width=8)
width.grid(row=1, column=1, sticky="w")
tk.Button(root, text="Обработать", command=run).grid(row=2, column=0, padx=10, pady=6, sticky="w")
listbox = tk.Listbox(root, width=60, height=12)
listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 10))
root.mainloop()
