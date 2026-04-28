from tkinter import ttk


class HomeWindow(ttk.Frame):
    def __init__(self, parent: ttk.Frame, store) -> None:
        super().__init__(parent)
        self.store = store

        self.columnconfigure(0, weight=1)

        ttk.Label(self, text="Welcome", style="Title.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(
            self,
            text="Simple and minimal library dashboard.",
            style="Subtitle.TLabel",
        ).grid(row=1, column=0, sticky="w", pady=(4, 16))

        self.stats_label = ttk.Label(self, text="", style="Subtitle.TLabel")
        self.stats_label.grid(row=2, column=0, sticky="w")

        ttk.Separator(self, orient="horizontal").grid(
            row=3, column=0, sticky="ew", pady=14
        )

        self.tips_label = ttk.Label(
            self,
            text=(
                "Use the left menu to add books, search, borrow/return, "
                "and check reports."
            ),
            wraplength=700,
        )
        self.tips_label.grid(row=4, column=0, sticky="w")

    def refresh(self) -> None:
        stats = self.store.get_stats()
        self.stats_label.config(
            text=(
                f"Total Books: {stats['total']}   |   "
                f"Available: {stats['available']}   |   "
                f"Borrowed: {stats['borrowed']}"
            )
        )
