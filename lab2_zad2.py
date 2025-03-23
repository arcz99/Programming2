class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent

class Komunikacja:
    def wyslij_wiadomosc(self, odbiorca, tresc):
        print(f"Wyslano wiadomosc do {odbiorca}: {tresc}")

class Rozrywka:
    def odtworz_muzyke(self, utwor):
        print(f"Odtwarzanie utworu: {utwor}")

class Smartphone:
    def __init__(self, model, producent):
        self.telefon = Telefon(model, producent)
        self.komunikacja = Komunikacja()
        self.rozrywka = Rozrywka()

smartfon1 = Smartphone("Galaxy s24","Samsung")
smartfon1.komunikacja.wyslij_wiadomosc("Jan","Czesc Janek")
smartfon1.rozrywka.odtworz_muzyke("Highway to Hell")
