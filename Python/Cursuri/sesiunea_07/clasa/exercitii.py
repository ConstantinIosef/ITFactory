"""Rezolvari exercitii Functii"""

"""
EX1: Defineste o functie care printeaza, pe rand,
primele 10 numere (1, 10).
"""
print("Rezolvare ex. 1")
def print_primele_10_numere():
    for numar in range(1, 11):
        print(numar)

print_primele_10_numere()

"""
EX2: Scrie o functie care parcurge o lista de numere data si
afiseaza mesajul 'Este par' pentru numerele pare si
'Este impar' pentru numere impare.
Daca in lista se gaseste un element care nu e numar intreg,
afiseaza un mesaj utilizatorului si apoi sari peste
elementul respectiv.
(Foloseste functia built-in isinstance()
pentru verificare daca elementul curent e int sau nu)
"""
print("Rezolvare ex. 2")


def verifica_lista_numere(lista):
    for i in range(len(lista)):
        if not isinstance(lista[i], int):
            print(f"elementul: {lista[i]} nu este un numar intreg")
            continue
        if lista[i] % 2 == 0:
            print(f"numarul este par {lista[i]}")
        else:
            print(f"numarul este impar {lista[i]}")


# def verifica_lista_numere(lista):
#     for i in range(len(lista)):
#         if isinstance(lista[i], int):
#
#             if lista[i] % 2 == 0:
#                 print(f"numarul este par {lista[i]}")
#             else:
#                 print(f"numarul este impar {lista[i]}")
#         else:
#             print(f"elementul: {lista[i]} nu este un numar intreg")
#

lista_numere = [-2.5, 4, 3, 5, 9, "3.5", "alabala"]
verifica_lista_numere(lista_numere)

"""
EX3: Scrie o functie care calculeaza patratul unui numar.
Afiseaza rezultatul.
"""
print("Rezolvare ex. 3")
def patratul_numar(numar):
    patrat = numar ** 2
    print(f"Patratul este : {patrat}")

patratul_numar(5)


"""
EX6: Rescrie functia de la exercitiul 3, 
astfel incat sa returneze rezultatul.
"""
print("Rezolvare ex. 6")
def patrat_numar(numar):
    return numar ** 2
print(f"Patratul este : {patrat_numar(4)}")


"""
EX8: Scrie o functie care ia ca parametru un numar intreg
si returneaza True daca numarul e par
si False daca numarul e impar.
"""
print("Rezolvare ex. 8")
def numar_intreg(numar: int):
    if numar % 2 == 0:
        return True
    else:
        return False

print(numar_intreg("14"))
