"""
EXERCITII WORKSHOP (Sesiunea 2)
"""


"""
NOTA: Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect vei exersa si operatorii in cadrul conditiilor ramurilor din if.

x poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte. 
X este un int.
"""


"""
1. Explica, cu cuvintele tale, in cadrul unui comentariu,
cum functioneaza un if else.
"""

# if else se foloseste atunci cand vrem sa facem o actiune bazata pe o conditie

"""
2. Verifica si afiseaza daca x este numar natural sau nu.
"""

ex2_x = int(input("Scrie un numar: "))

if ex2_x > 0:
    print(f"ex2_x = {ex2_x} deci este numar natural")
else:
    print(f"ex2_x = {ex2_x}, nu este numar natural")

"""
3. Verifica si afisează daca x este numar pozitiv, negativ sau neutru.
"""

ex3_x = int(input("Scrie un numar intreg pozitiv, negativ sau neutru: "))

if ex3_x > 0:
    print(f"ex3_x = {ex3_x} este numar pozitiv")
elif ex3_x < 0:
    print(f"ex3_x = {ex3_x} este numar negativ")
elif ex3_x == 0:
    print(f"ex3_x = {ex3_x} este numar neutru")
else:
    print("Esti tester.")

"""
4. Verifica si afisează daca x este intre -2 si 13.
"""

ex4_x = int(input("Scrie un numar intre -2 si 13: "))

if -2 > ex4_x > 13:
    print(f"ex4_x = {ex4_x} deci este intre -2 si 13")
else:
    print(f"ex4_x nu este intre -2 si 13")

"""
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5.
"""

ex5_x = int(input("Scrie un numar pentru variabila ex5_x: "))
ex5_y = int(input("Scrie un numar pentru variabila ex5_y: "))

ex5_diferenta = ex5_x - ex5_y

if ex5_diferenta < 5:
    print(f"Diferenta dintre ex5_x si ex5_y = {ex5_diferenta}, deci este mai mica decat 5")
else:
    print(f"Diferenta dintre ex5_x si ex5_y = {ex5_diferenta}, deci nu este mai mica de 5")


"""
6. Verifica daca x NU este intre 5 si 27  - a se folosi ‘not’.
"""

ex6_x = int(input("Scrie un numar intre 0 si 30: "))

if ex6_x not in range(5, 28):
    print(f"{ex6_x} nu este intre 5 si 27")
else:
    print(f"{ex6_x} este intre 5 si 27")

"""
7.
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu, afiseaza care din ele este mai mare.
"""

ex7_x = int(input("Scrie un numar pentru ex7_x: "))
ex7_y = int(input("Scrie un numar pentru ex7_y: "))

if ex7_x == ex7_y:
    print(f"{ex7_x} = {ex7_y}")
elif ex7_x > ex7_y:
    print(f"{ex7_x} > {ex7_y}")
elif ex7_x < ex7_y:
    print(f"{ex7_x} < {ex7_y}")
else:
    print("Esti tester.")