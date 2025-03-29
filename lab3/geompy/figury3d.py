import math

def szescian(bok):
    objetosci = bok ** 3
    pole_powierzchni = 6 * bok ** 2
    return objetosci, pole_powierzchni

def prostopadloscian(dlugosc, szerokosc, wysokosc):
    objetosci = dlugosc * szerokosc * wysokosc
    pole_powierzchni = 2 * (dlugosc * szerokosc + dlugosc * wysokosc + szerokosc * wysokosc)
    return objetosci, pole_powierzchni

def kula(promien):
    objetosci = (4/3) * math.pi * promien ** 3
    pole_powierzchni = 4 * math.pi * promien ** 2
    return objetosci, pole_powierzchni