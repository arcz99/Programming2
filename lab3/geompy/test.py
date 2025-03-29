from geompy import kwadrat, prostokat, kolo, szescian, prostopadloscian, kula

kwadrat_pole, kwadrat_obwod = kwadrat(4)
print(f"Kwadrat: pole = {kwadrat_pole}, obwód = {kwadrat_obwod}")

prostokat_pole, prostokat_obwod = prostokat(4, 6)
print(f"Prostokąt: pole = {prostokat_pole}, obwód = {prostokat_obwod}")

kolo_pole, kolo_obwod = kolo(3)
print(f"Koło: pole = {kolo_pole}, obwód = {kolo_obwod}")

# Testowanie funkcji z figury3d
szescian_objetosc, szescian_powierzchnia = szescian(3)
print(f"Sześcian: objętość = {szescian_objetosc}, pole powierzchni = {szescian_powierzchnia}")

prostopadloscian_objetosc, prostopadloscian_powierzchnia = prostopadloscian(3, 4, 5)
print(f"Prostopadłościan: objętość = {prostopadloscian_objetosc}, pole powierzchni = {prostopadloscian_powierzchnia}")

kula_objetosc, kula_powierzchnia = kula(3)
print(f"Kula: objętość = {kula_objetosc}, pole powierzchni = {kula_powierzchnia}")