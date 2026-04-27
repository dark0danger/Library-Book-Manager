import tkinter as tk
from tkinter import ttk

from data.book_store import BookStore
from styles.theme import apply_theme
from ui.windows.add_book_window import AddBookWindow
from ui.windows.borrow_return_window import BorrowReturnWindow
from ui.windows.home_window import HomeWindow
from ui.windows.reports_window import ReportsWindow
from ui.windows.search_window import SearchWindow


class LibraryApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Library Book Manager")
        self.geometry("980x620")
        self.minsize(860, 540)

        apply_theme(self)

        self.store = BookStore()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.nav_panel = ttk.Frame(self, padding=14, style="Card.TFrame")
        self.nav_panel.grid(row=0, column=0, sticky="ns", padx=12, pady=12)

        self.content_panel = ttk.Frame(self, padding=18)
        self.content_panel.grid(row=0, column=1, sticky="nsew", padx=(0, 12), pady=12)
        self.content_panel.grid_columnconfigure(0, weight=1)
        self.content_panel.grid_rowconfigure(0, weight=1)

        self.active_frame = None
        self.frames = {
            "Home": HomeWindow(self.content_panel, self.store),
            "Add Book": AddBookWindow(self.content_panel, self.store),
            "Search": SearchWindow(self.content_panel, self.store),
            "Borrow/Return": BorrowReturnWindow(self.content_panel, self.store),
            "Reports": ReportsWindow(self.content_panel, self.store),
        }

        self._build_nav()
        self.show_window("Home")

    def _build_nav(self) -> None:
        ttk.Label(self.nav_panel, text="Library Manager", style="Title.TLabel").pack(
            anchor="w", pady=(0, 14)
        )

        for label in self.frames:
            ttk.Button(
                self.nav_panel,
                text=label,
                style="Nav.TButton",
                command=lambda name=label: self.show_window(name),
            ).pack(fill="x", pady=4)

    def show_window(self, name: str) -> None:
        if self.active_frame is not None:
            self.active_frame.grid_forget()

        frame = self.frames[name]
        frame.grid(row=0, column=0, sticky="nsew")
        self.active_frame = frame

        for refresh_target in self.frames.values():
            refresh = getattr(refresh_target, "refresh", None)
            if callable(refresh):
                refresh()
