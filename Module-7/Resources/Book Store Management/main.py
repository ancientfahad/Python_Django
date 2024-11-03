import add_book
import view_all_books
import delete_book

all_books = []

print("Welcome To Book Store Management Project")

menu_text = """
Please Select an Option:
0. Exit
1. Add Book
2. View All Books
3. Delete Book
"""

while True:
    print(menu_text)
    menu = input("Input an Number: ")
    if menu == "0":
        break
    elif menu == "1":
        all_books = add_book.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = delete_book.delete_book(all_books)
    else:
        print("Invalid Input")