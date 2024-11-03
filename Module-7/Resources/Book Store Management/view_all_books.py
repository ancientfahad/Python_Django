def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f"Title:{book['title']} | Authors:{book['authors']} | ISBN:{book['isbn']}")
    else:
        print("No Book found in all_books files")