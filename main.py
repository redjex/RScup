import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import time

# Установка темы CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CustomTkinter App")
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.start_time = time.time()
        self.check_box = None

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
