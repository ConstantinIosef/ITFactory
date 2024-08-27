"""
EX1: Se da string-ul prop3 = 'Concertul va avea loc maine."
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""

ex1_prop3 = "Concertul va avea loc maine."
# a
ex1_prop3_primul_cuvant = ex1_prop3[0:9]
# b
print(f"primele 3 caractere din ex1_prop3 = {ex1_prop3[0:3]}")
# c
print(f"ex1_prop3 cu caractere inversate = {ex1_prop3[::-1]}")

"""
EX2: Se da variabila prop1 = 'Andy este prescurtarea de la Andrei"
a. Afiseaza primul caracter.
b. Afiseaza al 4-lea caracter.
c. Afiseaza ultimul caracter.
"""

ex2_prop1 = "Andy este prescurtarea de la Andrei"
# a
print(f"primul caracter din ex2_prop1 = {ex2_prop1[0:1]}")
# b
print(f"al 4-lea caracter din ex2_prop1 = {ex2_prop1[3:4]}")
# c
print(f"ultimul caracter din ex2_prop1 = {ex2_prop1[-1:]}")

"""
EX3: Se da string-ul prop2 = 'Masina e rosie.'
Afiseaza lungimea string-ului prop2.
"""

ex3_prop2 = "Masina e rosie."
print(f"lungimea stringului ex3_prop2 este de = {len(ex3_prop2)}")


"""
EX4: Se da string-ul my_str = 'vacanta'.
a. Foloseste metoda find() pentru a afla primul index la care se gaseste caracterul 'a'.
b. Foloseste metoda count() pentru a afla de cate ori apare caracterul 'a' in my_str.
c. Foloseste metoda capitalize() pentru a scrie cuvantul cu prima litera mare.
d. Foloseste metoda upper() pentru a scrie cuvantul cu litere mari.
"""

ex4_my_str = "vacanta"
# a
print(f"'a' se afla la indexul = {ex4_my_str.find("a")}")
# b
print(f"'a' apare de = {ex4_my_str.count("a")} ori")
# c
print(f"ex4_my_str + capitalize = {ex4_my_str.capitalize()}")
# d
print(f"ex4_my_str + upper = {ex4_my_str.upper()}")

"""
EX5: Exploreaza urmatoarele metode ajutatoare ale string-ului:
a. endswith()
b. index()
c. lower()
d. replace()
e. strip()
"""

ex5_str = "Banane sahariene."
ex5_list = ["banana", "ananas", "portocala", "pepene"]
# a
print(f"Metoda endswith ne ajuta sa aflam daca stringul se termina sau nu cu valoarea introdusa \n"
      f"ex5_str se termina cu 'e'? {ex5_str.endswith("e")}"
      )
# b
print(f"Metoda index ne afla pozitia unui string dintr-o lista \n"
      f"ex5_list are portocala ca pozitie = {ex5_list.index("portocala")}")
# c
print(f"Metoda lower forteaza toate caracterele din string sa fie scrise cu litera mica \n"
      f"ex5_str scris cu litera mica = {ex5_str.lower()}")
# d
print(f"Metoda replace ne ajuta sa inlocuim un cuvant din string \n"
      f"ex5_str 'sahariene' este inlocuit iar stringul acum este = {ex5_str.replace("sahariene", "arctice")}")
# e
print(f"Metoda strip ne ajuta sa stergem anumite caractere sau cuvinte din string \n"
      f"ex5_str fara sahariene. este = {ex5_str.strip("sahariene.")}")

"""
EX6: Se dau doua variabile, a = 10, b = 2.
Efectueaza toate operatiile pe cele 2 variabile,
folosind operatorii aritmetici.
"""

ex6_a = 10
ex6_b = 2

print(f"Adunare: {ex6_a+ex6_b} \n"
      f"Scadere: {ex6_a-ex6_b} \n"
      f"Inmultire: {ex6_a*ex6_b} \n"
      f"Impartire: {ex6_a/ex6_b}")

"""
EX7: Pentru fiecare din exemplele de mai jos, scrie intr-un comentariu
rezultatul asteptat, apoi decomenteaza codul de la fiecare exemplu, pe rand
si ruleaza exemplele si verifica output-ul.
"""

# Exemplul 1:
a = True
b = False
# print(not(a))
# print(not(b))

# Exemplul 2:
a = True
b = False
# x = not(a)
# y = not(b)
# print(a or b)
# print(x or y)
# print(a or x)
# print(x or b)

# Exemplul 3:
a = False
b = False
# x = not(a)
# y = not(b)
# print(a and b)
# print(a and x)
# print(y and b)
# print(x and y)



"""
EX8: Se da variabila num = 12
a. Verifica daca num citit este pozitiv.
b. verifica daca num este mai mare decat 5.
verifica daca num este mai mic decat 25.
c. verifica daca num este intre 0 si 20.
"""

ex8_num = 12

# a
if ex8_num > 0:
    print("Variabila ex8_num are un int pozitiv.")
elif ex8_num == 0:
    print("Variabila ex8_num este egala cu 0.")
else:
    print("Variabila ex8_num are un int negativ.")
# b
if ex8_num > 5:
    print("Variabila ex8_num este mai mare 5.")
else:
    print("Variabila ex8_num nu este mai mare de 5.")
# c
if 20 > ex8_num > 0:
    print("Variabila ex8_num este intre 0 si 20.")
else:
    print("Variabila ex8_num nu este intre 0 si 20.")


"""
EX9: Verifica daca varsta introdusa de utilizator este mai mare
decat 18 ani.
"""

ex9_varsta_user = int(input("Introdu varsta ta: "))
if ex9_varsta_user > 18:
    print("Varsta ta este mai mare de 18 ani.")
elif ex9_varsta_user == 18:
    print("Varsta ta este exact 18 ani.")
else:
    print("Varsta ta este sub 18 ani.")

"""
EX10: Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
"""

ex10_pret = int(input("Introdu pretul: "))

if ex10_pret <= 100:
    print("Pretul este mai mic sau egal cu 100 USD.")
else:
    print("Pretul este mai mare de 100 USD.")

"""
EX11:
a. Citeste un numar de la tastatura.
b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.
"""

ex11_numar = int(input("Introdu un numar: "))

if ex11_numar % 2 == 0:
    print(f"Numarul {ex11_numar} este par")
else:
    print(f"Numarul {ex11_numar} este impar")



"""
EX12:
a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
"""

ex12_viteza_medie = int(input("Care a fost viteza medie? "))
if 0 < ex12_viteza_medie <= 50:
    print("Viteza normala")
elif ex12_viteza_medie > 50:
    print("Viteza depasita")
else:
    print("Esti tester.")


"""
EX13: Citeste de la tastatura varsta utilizatorului si afiseaza categoria
de varsta in care se incadreaza.
Tine cont de aceste categorii de varsta:
- intre 0-18 ani: minor
- intre 18-65 ani: adult
- peste 65 ani: senior
"""

ex13_varsta_user = int(input("Introdu varsta ta: "))

if 0 < ex13_varsta_user < 18:
    print("Esti minor.")
elif 18 <= ex13_varsta_user < 65:
    print("Esti adult.")
elif 65 < ex13_varsta_user:
    print("Esti senior.")
else:
    print("Esti tester.")

"""
EX14: Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
cosul de cumparaturi, in functie de totalul cosului de cumparaturi
Reducerea se aplica in felul urmator:
- Total este intre 100 si 200 lei -> reducere 10%
- Total intre 200 - 300 lei -> reducere 15%
- Total intre 300-400 -> reducere 20 %
- Total mai mare de 400 -> reducere 30 %.
a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
dupa aplicarea reducerii.
"""

ex14_cos_cumparaturi = int(input("Care este totalul cosului de cumparaturi? "))
ex14_discount = 0

# a
if 100 < ex14_cos_cumparaturi < 200:
    ex14_discount = 0.1
elif 200 < ex14_cos_cumparaturi < 300:
    ex14_discount = 0.15
elif 300 < ex14_cos_cumparaturi < 400:
    ex14_discount = 0.2
elif ex14_cos_cumparaturi > 400:
    ex14_discount = 0.3
else:
    print(f"Esti tester, discountul tau este de {ex14_discount}%")
# b
if ex14_cos_cumparaturi < 0:
    print("Esti tester, nu primesti discount.")
else:
    ex14_pret_final = ex14_cos_cumparaturi - ex14_cos_cumparaturi * ex14_discount
    print(f"Valoarea finala dupa discount este de = {ex14_pret_final}")


