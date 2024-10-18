# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print(f"Название: {self.title}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

book = Book("Book", 1984, "Something", "Genre", "Someone", 1234)
print("\nДанные о книге:")
book.display_data()
book.input_data()
print("\nИзменённые данные о книге:")
book.display_data()

print(f"Название: {book.get_title()}")
print(f"Год выпуска: {book.get_year()}")
print(f"Издатель: {book.get_publisher()}")
print(f"Жанр: {book.get_genre()}")
print(f"Автор: {book.get_author()}")
print(f"Цена: {book.get_price()}")