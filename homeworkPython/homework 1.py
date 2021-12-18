class Book:
    NameBook = 'Автостопом по Галактике'
    ReleaseBooK = '2019'
    Publisher = "ACT Москва"
    Genre = "Фантастический роман"
    Author = "Дуглас Адамс"
    Price = "750"

    def print_info(self):
        print(f'Название книги: {self.NameBook}\nГод выпуска: {self.ReleaseBooK} год\n'
              f'Издатель: {self.Publisher}\nЖанр: {self.Genre}\n'
              f'Автор: {self.Author}\nЦена: {self.Price} рублей')

    def input_info(self, NameBook, ReleaseBooK, Publishe, Genre, Author, Price):
        self.NameBook = NameBook
        self.ReleaseBooK = ReleaseBooK
        self.Publisher = Publishe
        self.Genre = Genre
        self.Author = Author
        self.Price = Price

    def set_name(self, NameBook):
        self.NameBook = NameBook

    def get_name(self):
        return self.NameBook

    def set_release(self, ReleaseBooK):
        self.ReleaseBooK = ReleaseBooK

    def get_release(self):
        return self.ReleaseBooK

    def set_publisher(self, Publisher):
        self.Publisher = Publisher

    def get_publisher(self):
        return self.Publisher

    def set_genre(self, Genre):
        self.Genre = Genre

    def get_genre(self):
        return self.Genre

    def set_author(self, Author):
        self.Author = Author

    def get_author(self):
        return self.Author

    def set_price(self, Price):
        self.Price = Price

    def get_price(self):
        return self.Price


b = Book()
b.print_info()
print('\nВывод к отдельным полям:')
print(b.get_name())
print(b.get_release())
print(b.get_publisher())
print(b.get_genre())
print(b.get_author())
print(b.get_price())