"""
quiz333
q4
"""

books = [
    {"title": "Book A", "author": "Author 1", "copies": 3},
    {"title": "Book B", "author": "Author 2", "copies": 5},
    {"title": "Book C", "author": "Author 1", "copies": 2},
    {"title": "Book D", "author": "Author 3", "copies": 4},
    {"title": "Book A", "author": "Author 3", "copies": 3},
    {"title": "Book B", "author": "Author 1", "copies": 5},
    {"title": "Book C", "author": "Author 1", "copies": 2},
    {"title": "Book D", "author": "Author 2", "copies": 4},
]

author_to_search = "Author 2"
book_name_list = []
qty_of_available = 0

for book in books:
    # print(book)
    if book["author"] == author_to_search:
        book_name_list.append(book["title"])
        qty_of_available += book["copies"]

if qty_of_available:
    print(f"Books by {author_to_search}:")
    for book_name in set(book_name_list):
        print(f"- {book_name}")
    print(f"Total copies available: {qty_of_available}")
else:
    print("No such author, please search again.")
