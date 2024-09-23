import tkinter as tk
import customtkinter as ctk
import time
from tkinter import messagebox
import os

# Установка темы CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("RScup")
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.root.geometry("400x400")
        self.start_time = time.time()
        self.check_box = None
        self.show_check_box_after_delay()
        self.minimize_after_delay()  # Добавление функции сворачивания окна через 15 секунд

    def show_check_box_after_delay(self):
        self.root.after(5000, self.show_check_box)  # Появление чекбокса через 5 секунд

    def show_check_box(self):
        self.check_box = ctk.CTkCheckBox(master=self.frame, text="RScup\nПроверка...")
        self.check_box.pack(pady=20)
        self.check_box.bind("<Button-1>", self.check_box_clicked)

    def check_box_clicked(self, event):
        elapsed_time = (time.time() - self.start_time) * 1000  # Время в миллисекундах
        if elapsed_time >= 130:
            os.system("python main.py")  # Открываем файл main.py
            self.root.destroy()  # Закрываем текущее окно
        else:
            messagebox.showerror("Error", f"Could not open main.py:")

    def minimize_after_delay(self):
        self.root.after(15000, self.minimize_window)  # Сворачивание окна через 15 секунд

    def minimize_window(self):
        self.root.iconify()  # Сворачиваем окно

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
