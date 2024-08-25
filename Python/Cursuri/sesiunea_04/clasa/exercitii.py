"""
EX8:
a. Citeste de la tastatura urmatoarele date legate de o noua reteta: nume,
ingrediente, timp prepapare.
b. Salveaza datele citite intr-un dictionar.
c. Actualizeaza numele retetei, scriind-ul cu litere mari.
"""

# print("rezolvare ex 8")
# #pct a
# nume = input("Scrie numele retetei: ")
# ingrediente = input("Scrie ingredientele: ")
# timp_preparare = input("Scrie timpul de preparare: ")
#
# #pct b
# reteta = {
#     "nume": nume,
#     "ingrediente": ingrediente,
#     "timp_preparare": timp_preparare
# }
# print(reteta)
#
# #pct c
# reteta["nume"] = reteta["nume"].upper()
# print(reteta)


"""
EX2:
a. Defineste o lista numita filme_preferate, cu cel putin 3 elemente.
b. Inverseaza lista folosind slicing. (ca la string)
c. Folosind if, verifica daca lista este goala sau nu,
si afiseaza un mesaj corespunzator pentru fiecare situatie.
"""

print("rezolvare ex 2")
#pct a
filme_preferate = ["Titanic", "Avatar", "Cenusareasa"]
print(filme_preferate)

#pct b
lista_filme_preferate_inversate = filme_preferate[::-1]
print(lista_filme_preferate_inversate)

#pct c

if len(filme_preferate) == 0:
    print("lista este goala")
else:
    print("Lista are elemente")

"""
EX5: Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""
print("rezolvare ex 5")
my_set = {1, 2, 3, 4}
print(my_set)
my_set.add(5) #pct a
my_set.add(6) #pct b
my_set.add(1) #pct c
my_set.remove(3) #pct d
my_set.pop() #pct e
print(my_set)

"""
EX6:
Se da urmatoarea structura de date:
locatie = (44.34, 12.456)
a. Verifica tipul structurii de date
b. Este aceasta structura de date ordonata?
c. Este aceasta structura de date mutabila?
d. Determina lungimea structurii de date.
e. Salveaza a doua valoare intr-o variabila.
Verifica daca aceasta este mai mare de 13, si afiseaza
un mesaj corespunzator.
"""
print("Rezolvare ex 6")

locatie = (44.34, 12.456)

print(type(locatie))   #pct a
# pct b - Da, este ordonata
# pct c - Nu, este mutabila

#pct d
print(f"Lungimea structurii de date din variabila 'locatie' este de: {len(locatie)} elemente ")

#pct 3
var_2 = locatie[1]

if var_2 > 13:
    print("Variabila este mai mare decat 13")
else:
    print("Variabila este mai mica decat 13")





