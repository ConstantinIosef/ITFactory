"""
EX1: Defineste o functie care printeaza, pe rand,
primele 10 numere (1, 10).
"""

def print_first_10_numbers():
    for number in range(1, 11):
        print(number)

print_first_10_numbers()

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

