from tkinter import messagebox, ttk


class BorrowReturnWindow(ttk.Frame):
    def __init__(self, parent: ttk.Frame, store) -> None:
        super().__init__(parent)
        self.store = store

        style = ttk.Style(self)
        style.configure("Books.Treeview", rowheight=28, font=("Helvetica", 10))
        style.configure("Books.Treeview.Heading", font=("Helvetica", 10, "bold"))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        ttk.Label(self, text="Borrow / Return", style="Title.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 10)
        )

        table_frame = ttk.Frame(self)
        table_frame.grid(row=1, column=0, sticky="nsew")
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("id", "title", "status"),
            show="headings",
            style="Books.Treeview",
        )
        self.tree.grid(row=0, column=0, sticky="nsew")

        y_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        y_scroll.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=y_scroll.set)

        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Title")
        self.tree.heading("status", text="Status")

        self.tree.column("id", width=60, anchor="center", stretch=False)
        self.tree.column("title", width=450, stretch=True)
        self.tree.column("status", width=120, anchor="center", stretch=False)

        actions = ttk.Frame(self)
        actions.grid(row=2, column=0, sticky="w", pady=10)

        ttk.Button(actions, text="Borrow", command=self.borrow_selected).grid(
            row=0, column=0, padx=(0, 8)
        )
        ttk.Button(actions, text="Return", command=self.return_selected).grid(
            row=0, column=1
        )
        ttk.Button(actions, text="Delete", command=self.delete_selected).grid(
            row=0, column=2, padx=(8, 0)
        )

    def _get_selected_book_id(self) -> int | None:
        selected = self.tree.selection()
        if not selected:
            return None
        values = self.tree.item(selected[0], "values")
        return int(values[0])

    def borrow_selected(self) -> None:
        book_id = self._get_selected_book_id()
        if book_id is None:
            messagebox.showerror("Error", "Select a book first.")
            return

        if self.store.borrow_book(book_id):
            messagebox.showinfo("Success", "Book borrowed.")
        else:
            messagebox.showerror("Error", "Book is already borrowed.")

        self.refresh()

    def return_selected(self) -> None:
        book_id = self._get_selected_book_id()
        if book_id is None:
            messagebox.showerror("Error", "Select a book first.")
            return

        if self.store.return_book(book_id):
            messagebox.showinfo("Success", "Book returned.")
        else:
            messagebox.showerror("Error", "Book is already available.")

        self.refresh()

    def delete_selected(self) -> None:
        book_id = self._get_selected_book_id()
        if book_id is None:
            messagebox.showerror("Error", "Select a book first.")
            return

        confirmed = messagebox.askyesno(
            "Confirm Delete", "Are you sure you want to delete this book?"
        )
        if not confirmed:
            return

        if self.store.delete_book(book_id):
            messagebox.showinfo("Success", "Book deleted.")
        else:
            messagebox.showerror("Error", "Book not found.")

        self.refresh()

    def refresh(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)

        for book in self.store.get_all_books():
            status = "Borrowed" if book.is_borrowed else "Available"
            self.tree.insert("", "end", values=(book.book_id, book.title, status))
