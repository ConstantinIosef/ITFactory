"""
EXERCITII WORKSHOP (Sesiunea 1)
"""


"""
1. In cadrul unui comentariu, explica in cuvintele tale ce este o variabila.
"""

# O variabila este un obiect care poate fi schimbat

"""
2. Declara si initializeaza cate o variabila din fiecare din urmatoarele tipuri de date:
- string
- int 
- float
- bool

OBSERVATIE: Valorile vor fi alese de tine, dupa preferinte.
"""

ex2_string = "this is a string"
ex2_int = 10
ex2_float = float(10.8)
ex2_bool = bool(10)

"""
3. Utilizeaza functia type pentru a verifica daca variabilele definite la exercitiul 2 au tipul de date asteptat.
"""

print(type(ex2_string))
print(type(ex2_int))
print(type(ex2_float))
print(type(ex2_bool))

"""
4. 
a. Rotunjeste variabila de tip float definita la exercitiul 2, folosind functia round(),
si salveaza aceasta modificare in aceeasi variabila (SUPRASCRIERE).
b. Verifica si afiseaza tipul acesteia.
"""

ex2_float = ex2_float.__round__()
print(type(ex2_float))
print(f"ex2_float este rotunjit la numarul: {ex2_float}")

"""
5. Foloseste functia print() si afiseaza in consola 4 propozitii,
folosind cele 4 variabile declarate la exercitiul 2. 
Rezolva nepotrivirile de tip prin ce modalitate doresti.
"""

print(
    f"ex2_string este un string cu valoarea = '{ex2_string}' \n"
    f"ex2_int este un integer cu valoarea = '{ex2_int}' \n"
    f"ex2_float este un float cu valoarea = '{ex2_float}' \n"
    f"ex2_bool este un boolean cu valoarea = '{ex2_bool}' \n"
)

"""
6. Citeste de la tastatura:
- numele utilizatorului
- prenumele utilizatorului

Afiseaza propozitia 'Numele complet are x caractere',
unde x reprezinta numarul total de caractere din numele complet
al utilizatorului.
"""

ex6_nume_user = input("Scrie numele tau: ")
ex6_prenume_user = input("Scrie prenumele tau: ")
ex6_total_caractere = len(ex6_nume_user+ex6_prenume_user)

print(f"Numele complet are {ex6_total_caractere} caractere")
