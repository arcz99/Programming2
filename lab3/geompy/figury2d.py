import math


def kwadrat(bok):
    pole = bok ** 2
    obwod = 4 * bok
    return pole, obwod

def prostokat(dlugosc, szerokosc):
    pole = dlugosc * szerokosc
    obwod = 2 * (dlugosc + szerokosc)
    return pole, obwod

def kolo(promien):
    pole = math.pi * promien ** 2
    obwod = 2 * math.pi * promien
    return pole, obwod