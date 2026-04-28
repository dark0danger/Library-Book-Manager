from tkinter import messagebox, ttk


class AddBookWindow(ttk.Frame):
    def __init__(self, parent: ttk.Frame, store) -> None:
        super().__init__(parent)
        self.store = store

        self.columnconfigure(1, weight=1)

        ttk.Label(self, text="Add Book", style="Title.TLabel").grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 14)
        )

        ttk.Label(self, text="Title").grid(row=1, column=0, sticky="w", pady=6)
        self.title_var = ttk.Entry(self)
        self.title_var.grid(row=1, column=1, sticky="ew", pady=6)

        ttk.Label(self, text="Author").grid(row=2, column=0, sticky="w", pady=6)
        self.author_var = ttk.Entry(self)
        self.author_var.grid(row=2, column=1, sticky="ew", pady=6)

        ttk.Label(self, text="Year").grid(row=3, column=0, sticky="w", pady=6)
        self.year_var = ttk.Entry(self)
        self.year_var.grid(row=3, column=1, sticky="ew", pady=6)

        ttk.Button(
            self, text="Add", style="Primary.TButton", command=self.add_book
        ).grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 0))

    def add_book(self) -> None:
        title = self.title_var.get().strip()
        author = self.author_var.get().strip()
        year_text = self.year_var.get().strip()

        if not title or not author or not year_text:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        if not year_text.isdigit():
            messagebox.showerror("Error", "Year must be a number.")
            return

        self.store.add_book(title, author, int(year_text))
        messagebox.showinfo("Success", "Book added.")

        self.title_var.delete(0, "end")
        self.author_var.delete(0, "end")
        self.year_var.delete(0, "end")
