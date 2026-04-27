from tkinter import ttk


class ReportsWindow(ttk.Frame):
    def __init__(self, parent: ttk.Frame, store) -> None:
        super().__init__(parent)
        self.store = store

        ttk.Label(self, text="Reports", style="Title.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 12)
        )

        self.total_label = ttk.Label(self, text="")
        self.total_label.grid(row=1, column=0, sticky="w", pady=4)

        self.available_label = ttk.Label(self, text="")
        self.available_label.grid(row=2, column=0, sticky="w", pady=4)

        self.borrowed_label = ttk.Label(self, text="")
        self.borrowed_label.grid(row=3, column=0, sticky="w", pady=4)

    def refresh(self) -> None:
        stats = self.store.get_stats()
        self.total_label.config(text=f"Total books: {stats['total']}")
        self.available_label.config(text=f"Available books: {stats['available']}")
        self.borrowed_label.config(text=f"Borrowed books: {stats['borrowed']}")