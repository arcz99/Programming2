class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
    def opis(self):
        return f" '{self.tytul}' {self.autor} {self.rok_wydania}"

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku
    def opis(self):
        return f"{super().opis()} Plik ma rozmiar {self.rozmiar_pliku}"


class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania
    def opis(self):
        return f"{super().opis()} Czas trwania : {self.czas_trwania}"



ksiazka1 = Ksiazka("Lalka", "Prus", "1890")

ebook1 = Ebook("Lalka", "Prus", "2020", 40)

audiobook = Audiobook("Lalka", "Prus", "2017", 540)



print(ksiazka1.opis())
print(ebook1.opis())
print(audiobook.opis())