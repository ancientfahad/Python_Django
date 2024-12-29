from save_all_books import save_all_books

def delete_book(all_books):
    # found_search_result = False
    
    search_item = input("Enter title or ISBN or Author's name for Delete book: ")
    
    matching_books = []
    
    for index, book in enumerate(all_books):
        if(search_item.lower() in book["title"].lower() or search_item.lower() in book["authors"].lower() or search_item.lower() in book["isbn"]):
            found_search_result = True
            matching_books.append((index, book))
            
            print (f"{len(matching_books)}. Title: {book['title']} - Authors: {book['authors']} - ISBN: {book['isbn']} - Price: {book['price']} - Quantity: {book['quantity']}")
            
    if not found_search_result:
        print("No books found to remove ")
        return all_books
    
    try:
        selected_index = int(input("Enter the Index number of the book which you want to remove: "))
        
        if selected_index <= 0:
            raise IndexError
        
        book_index = matching_books [selected_index - 1] [0]
        book_to_delete = all_books [book_index]
        
        all_books.pop(book_index)
        save_all_books(all_books)
        print(f"'{book_to_delete['title']}' has been deleted.")
        
    except(IndexError, ValueError):
        print("Invalid Input")
        
    return all_books
        
        
            
            