"""
EXERCITII WORKSHOP (Sesiunea 3)
"""


"""
1.
a. Citeste un string de la tastatura (ex: alabala portocala).
b. Salveaza primul caracter intr-o variabila - indiferent care este el, incearca cu 2 string-uri diferite.
c. Capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter => alAbAlA portocAla.
"""

# a
ex1_string = input("Scrie 2-3 cuvinte: ")
# b
ex1_primul_caracter = ex1_string[0]
# c
ex1_string_list = list(ex1_string)

for i in range(1, len(ex1_string_list) - 1):
    if ex1_string_list[i] == ex1_primul_caracter:
        ex1_string_list[i] = ex1_string_list[i].upper()

ex1_string_final = ''.join(ex1_string_list)

print("Rezultatul este: ", ex1_string_final)

"""
2.
a. Citeste un username de la tastatura.
b. Citeste o parola.
c. Afiseaza: 'Parola pentru user-ul x este ***** și are x caractere'.
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect.

Exemple:
- parola 'abc' => ***
- parola 'abcd' => ****
"""

# a
ex2_username = input("Scrie un username: ")
# b
ex2_password = input("Scie o parola: ")
# c
ex2_password_hidden = len(ex2_password)

print(f"Parola pentru userul {ex2_username} este {ex2_password_hidden * "*"}")

"""
3. 
x, y, z - laturile unui triunghi.
Afișeaza daca triunghiul este isoscel, echilateral sau oarecare.
"""

ex3_x = input("Scrie latura X a unui triunghi: ")
ex3_y = input("Scrie latura Y a unui triunghi: ")
ex3_z = input("Scrie latura Z a unui triunghi: ")

if ex3_x == ex3_y == ex3_z:
    print("Triunghiul este echilateral.")
elif ex3_x == ex3_z:
    print("Triunghiul este isoscel.")
elif ex3_x == ex3_y:
    print("Triunghiul este isoscel.")
elif ex3_y == ex3_z:
    print("Triunghiul este isoscel.")
else:
    print("Triunghiul este oarecare")

"""
4.
a. Citeste un numar intreg, x, de la tastatura.
b. Verifica daca x are exact 6 cifre.
"""

# a
ex4_numar_intreg = input("Scrie orice numar intreg: ")

try:
    ex4_numar_intreg = int(ex4_numar_intreg)
except ValueError:
    print("Nu ai introdus un numar intreg valid.")
    exit()

# b
ex4_numar_intreg_string = str(abs(ex4_numar_intreg))

if len(ex4_numar_intreg_string) == 6:
    print(f"ex4_numar_intreg are {len(ex4_numar_intreg_string)} deci are exact 6 cifre")
else:
    print("ex4_numar_intreg nu are exact 6 cifre")

"""
5. 
a. Citeste trei numere intregi, x, y, z, de la tastatura.
b. Afiseaza care este cel mai mare dintre ele.
"""

# a
ex5_x = int(input("Scrie un numar intreg pentru X: "))
ex5_y = int(input("Scrie un numar intreg pentru Y: "))
ex5_z = int(input("Scrie un numar intreg pentru Z: "))

# b

if ex5_x > ex5_y and ex5_x > ex5_z:
    print("X este cel mai mare numar intreg dintre XYZ.")
elif ex5_y > ex5_x and ex5_y > ex5_z:
    print("Y este cel mai mare numar intreg dintre XYZ.")
elif ex5_z > ex5_x and ex5_z > ex5_y:
    print("Z este cel mai mare numar intreg dintre XYZ.")
elif ex5_x == ex5_y == ex5_z:
    print("XYZ sunt egale.")
else:
    print("Esti tester.")


"""
6. Avand string-ul: 'Coral is either the stupidest animal or the smartest rock':
Declara un string nou care sa fie format din primele 5 caractere + ultimele 5.
"""

ex6_string = "Coral is either the stupidest animal or the smartest rock"
ex6_string_first = ex6_string[:5]
ex6_string_last = ex6_string[-5:]
ex6_string_final = ex6_string_first + ex6_string_last

print(f"Noul string este = '{ex6_string_final}'")

"""
7. Avand string-ul '0123456789':
- Afiseaza doar numerele pare. 
- Afiseaza doar numerele impare.

HINT: Foloseste slicing, controleaza din pas
"""

ex7_string = "0123456789"
ex7_numere_pare = 0
ex7_numere_impare = 0

# numere pare
ex7_numere_pare = ex7_string[::2]

# numere impare
ex7_numere_impare = ex7_string[1::2]

# rezultat
print(f"Numerele pare sunt {ex7_numere_pare}")
print(f"Numerele impare sunt: {ex7_numere_impare}")


"""
EXERCITII RECOMANDATE - STUDIU INDIVIDUAL                                        .

1. Revizualizeaza sesiunile din aceasta saptamana si ia notite in caz ca ti-a scapat ceva.

2. Vizualizeaza din cursul ‘Primii pasi in Programare’ sectiunile:
- Variabile si Tipuri de date
- Operatori si Flow Control.
"""
