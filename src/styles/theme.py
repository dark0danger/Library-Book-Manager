import tkinter as tk
from tkinter import ttk


def apply_theme(root: tk.Tk) -> None:
    style = ttk.Style(root)
    style.theme_use("clam")

    root.configure(bg="#f5f7fa")

    style.configure("Title.TLabel", font=("Helvetica", 18, "bold"), foreground="#1f2937")
    style.configure("Subtitle.TLabel", font=("Helvetica", 12), foreground="#4b5563")
    style.configure("Card.TFrame", background="#ffffff")
    style.configure("Nav.TButton", font=("Helvetica", 11), padding=8)
    style.configure("Primary.TButton", font=("Helvetica", 10, "bold"), padding=8)
    style.configure("TLabel", background="#f5f7fa")
    style.configure("TFrame", background="#f5f7fa")
