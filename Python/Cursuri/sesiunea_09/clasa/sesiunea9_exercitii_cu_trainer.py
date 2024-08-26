"""
Sesiunea 9 - Exercitii cu Trainer
"""


"""
IMPORTANT! Pentru toate exercitiile: apelati functia de cel putin 2 ori
cu valori diferite pentru a testa.
Daca functia are return, printeaza raspunsul.                        
"""


"""
1. Functie care returneaza aria dreptunghiului.
"""

latime = int(input("Care este latimea dreptunghiului? \n"))
lungime = int(input("Care este lungimea dreptunghiului? \n"))

def aria_dreptunghiului(latime,lungime):
    return latime * lungime

print("Aria dreptunghiului este ", {aria_dreptunghiului(latime,lungime)})

"""
2. Functie care returneaza True daca un caracter x se gaseste intr-un string dat
si False daca nu se gaseste.
"""
# VARIANTA C
#
# litera = input("Introduceti un caracter: ").lower()
# cuvant = input("Introduceti un cuvant: ").lower()
# def verificare_caracter(litera,cuvant):
#     if litera in cuvant:
#         return True
#     else:
#         return False
# verificare_caracter(litera,cuvant)
# print(verificare_caracter(litera,cuvant))
# print(cuvant.find(litera))


# VARIANTA B
#
# litera = input("Introduceti un caracter: ").lower()
# cuvant = input("Introduceti un cuvant: ").lower()
#
# def verificare_caracter(litera,cuvant):
#     for caracter in cuvant:
#         if caracter == litera:
#             return True
#         else:
#             return False
#
# verificare_caracter(litera,cuvant)
# print(verificare_caracter(litera,cuvant))
# print(cuvant.find(litera))


# VARIANTA C

litera = input("Introduceti un caracter: ").lower()
cuvant = input("Introduceti un cuvant: ").lower()

def verificare_caracter(litera,cuvant):
    if cuvant.find(litera) != -1:
        return True
    else:
        return False

verificare_caracter(litera,cuvant)
print(verificare_caracter(litera,cuvant))
print(cuvant.find(litera))

"""
3. Functie care nu returneaza nimic. Primeste doua numere si PRINTEAZA:
Primul numar x este mai mare decat al doilea numar y
Al doilea numar y este mai mare decat primul numar x
Numerele sunt egale. 
"""


def compara_numere(ex3_x,ex3_y):
    if ex3_x > ex3_y:
        print(f"Primul numar {ex3_x} este mai mare decat al doilea numar {ex3_y}")
    elif ex3_y > ex3_x:
        print(f"Al doilea numar {ex3_y} este mai mare decat primul numar {ex3_x}")
    else:
        print("Numerele sunt egale")

compara_numere(20,5)
compara_numere(3,16)
compara_numere(4,4)

"""
4. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Printeaza ‘nu am adaugat numarul in set. Acesta există deja’ + returneaza False
"""



"""
5. Functie care primeste o luna din an si returneaza cate zile are acea luna.
"""



"""
6. Functie calculator care sa returneze 4 valori: Suma, diferenta, inmulțirea, impartirea a doua numere.

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""



"""
7. Functie care primeste o lista de cifre (adica doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""



"""
8. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
"""



"""
9. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: dacă dam numarul 3, suma va fi 6 (0+1+2+3)
"""



"""
10. Functie care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
"""



"""
11. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90 de lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.
"""



"""
12. Funcție care sa afiseze data si ora curenta din Romania.
(bonus: afiseaza si data si ora curenta din China)
"""



"""
13. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la Craciun
daca nu vrei sa ne zici cand e ziua ta :)
"""

from datetime import datetime

def zile_pana_craciun():
    ex13_astazi = datetime.now()
    ex13_data_craciun = datetime(ex13_astazi.year,12,25)
    if ex13_astazi > ex13_data_craciun:
        ex13_data_craciun = datetime(ex13_astazi.year + 1,12,25)
    zile_pana_craciun = ex13_data_craciun - ex13_astazi
    print(f"Mai sunt {zile_pana_craciun} zile pana la craciun")

zile_pana_craciun()