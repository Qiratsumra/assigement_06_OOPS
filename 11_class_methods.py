# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    total_books = 0
    def __init__(self,title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
    @classmethod
    def increment_book_count (cls):
        cls.total_books += 1
book1 = Book('Pir-e-kamil', 'Nimra Ahmed')
book2 = Book('Pir-e-kamil', 'Nimra Ahmed')
book3 = Book('Pir-e-kamil', 'Nimra Ahmed')
print(book1.total_books)
print(book2.total_books)
print(book3.total_books)