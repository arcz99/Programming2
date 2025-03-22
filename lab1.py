import json

class ModelAI:
    liczba_modeli = 0  #

    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        ModelAI.nowy_model()

    @classmethod
    def nowy_model(cls):
        cls.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        try:
            with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
                dane = json.load(plik)
                return cls(dane['name'], dane['version'])
        except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
            print(f"Błąd podczas wczytywania modelu: {e}")
            return None

if __name__ == "__main__":
    model1 = ModelAI("GPT-4", "1.0")
    print(f"Liczba modeli: {ModelAI.ile_modeli()}")

    model2 = ModelAI.z_pliku("model.json")
    if model2:
        print(f"Utworzono model: {model2.nazwa_modelu}, wersja: {model2.wersja}")
    print(f"Liczba modeli: {ModelAI.ile_modeli()}")