"""
EX1:
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""
# a
ex1_latime = 2
# b
ex1_descriere = "This is a description."
# c
ex1_pret = float(100)
ex1_discount = float(20)
# d
ex1_initializat = "Ananas"

# e
print(ex1_latime)
print(ex1_descriere)
print(ex1_pret)
print(ex1_discount)
print(bool(ex1_initializat))

"""
EX2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10.
"""

ex2_var1, ex2_var2 = 10, 10

print(ex2_var1)
print(ex2_var2)


"""
EX3: Folosind o singura linie de cod, initializeaza/ defineste doua variabile de tip string cu valori diferite.
"""

ex3_var1, ex3_var2 = "ex3_var1", "ex3_var2"

print(ex3_var1)
print(ex3_var2)

"""
EX4: Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
Afiseaza in consola un mesaj care sa contina cele doua variabile.
"""

ex4_nume = "nume"
ex4_pret = "pret"

print(ex4_pret + " " + ex4_nume)

"""
EX5:
a. Defineste doua variabile: nume (string) si varsta (int).
b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
"""

ex5_string = "John"
ex5_varsta = 40

print(f"{ex5_string} are {ex5_varsta} de ani")

"""
EX6:
a. Defineste o variabila de tip int, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
b. Defineste o variabila de tip float, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
c. Defineste o variabila de tip string, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
d. Defineste o variabila de tip bool, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
"""

# a
ex6_int = 10
print(ex6_int)
print(type(ex6_int))
# b
ex6_float = float(10.1)
print(ex6_float)
print(type(ex6_float))
# c
ex6_string = "zece"
print(ex6_string)
print(type(ex6_string))
# d
ex6_bool = bool(10)
print(ex6_bool)
print(type(ex6_bool))

"""
EX7: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""

# a
ex7_int = 10
print(ex7_int)
# b
print(type(ex7_int))
# c
ex7_float = float(ex7_int)
# d
print(ex7_float + 0.1)

"""
EX8:
a. Defineste o variabila de tip string. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de la punctul a, in int si salveaza rezultatul intr-o noua variabila.
Ruleaza programul.
Ce observi?
"""
# a
ex8_string = "10"
print(ex8_string)
# b
print(type(ex8_string))
# c
ex8_int = int(ex8_string)
print(ex8_int)
# un STRING poate sa fie transformat in INTEGER doar daca acesta are cifre

"""
EX9: Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""

ex9_variable = input("Introdu un numar: ")
print("Numarul pe care l-ai introdus este:", ex9_variable)

"""
EX10: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""

ex10_pret = int(input("Cat costa o ceapa? Introdu un numar "))
print(f"O ceapa costa {ex10_pret} RON!")
