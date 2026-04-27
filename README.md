# Library-Book-Manager
Simple and minimal Library Book Manager desktop app built with Python and Tkinter, featuring 5 windows: Home, Add Book, Search, Borrow/Return, and Reports.


# ShelfFive

Simple and minimal Python GUI app for managing library books.

## Project Idea
- App topic: Library Book Manager
- GUI style: Simple and Minimal
- Windows count: 5

## Windows
1. Home
2. Add Book
3. Search Books
4. Borrow / Return
5. Reports

## Run
```bash
cd /home/mohammed-nasser/Moageza/fuck/library-book-manager/src
python app.py
```

If `python` is not available on your VM, use `python3`.

## Team Split (8 Members)
Each member creates a branch and works on assigned files.

1. john
- `src/models/book.py`

2. muhammed
- `src/data/book_store.py`

3. hamza
- `src/ui/windows/home_window.py`

4. david
- `src/ui/windows/add_book_window.py`

5. youssef
- `src/ui/windows/search_window.py`

6. eslam
- `src/ui/windows/borrow_return_window.py`

7. amen
- `src/ui/windows/reports_window.py`

8. sgood
- `src/ui/main_window.py`

## GitHub Workflow in VMs
1. Clone repo in each VM.
2. Create branch:
```bash
git checkout -b feature/<name>-part
```
3. Make changes only in assigned files.
4. Commit:
```bash
git add .
git commit -m "Add <part> by <name>"
```
5. Push:
```bash
git push -u origin feature/<name>-part
```
6. Open Pull Request to `main`.
7. Team lead reviews and merges.

## Suggested Branch Names
- `feature/john-model`
- `feature/muhammed-store`
- `feature/hamza-home-window`
- `feature/david-add-book-window`
- `feature/youssef-search-window`
- `feature/eslam-borrow-return-window`
- `feature/amen-reports-window`
- `feature/sgood-main-shell`
