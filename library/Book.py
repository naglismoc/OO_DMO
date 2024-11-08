class Book():
    def __int__(self, title="", author="", pages=0, release_year=0, price=0):
        self.Title = title
        self.Author = author
        self.Pages = pages
        self.RelesaseYear = release_year
        self.Price = price

    def name_case(self, title):
        return title[0].upper() + title[1:].lower()

    @property #getter
    def Title(self):
        return self._Title.lower()

    @Title.setter #setter
    def Title(self, title):
        self._Title = self.name_case(title)

    def __str__(self):
        return f'{self._Title} {self.Author} {self.Pages} {self.RelesaseYear} {self.Price}'

    def pagePrice(self):
        return self.Price / self.Pages if self.Pages > 0 else 1

    def prettify(self):
        return f'Knygos "{self._Title}" autorius yra {self.Author}. Knyga turi {self.Price} puslapių ir yra išleista {self.RelesaseYear} metais.'
