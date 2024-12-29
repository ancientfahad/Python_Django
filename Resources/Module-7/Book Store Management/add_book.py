from save_all_books import save_all_books

def add_books(all_books):
    title = input("Enter Book Title: ")
    while True:
        authors = input("Enter Multiple authors name by using semicolon (;) : ")
        if ',' in authors:
            print("Can't use Comma. Please use Semicolon(;)")
        else:
            break
    isbn = input("Enter ISBN number: ")
    year = input("Enter pulishing year: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    
    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }
    
    all_books.append(book)
    save_all_books(all_books)
    
    print("Books Added Successfully")
    
    return all_books