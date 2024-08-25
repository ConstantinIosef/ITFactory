"""
Obiective curs: Variable, tipuri de date
Setup functional
Principii de baza in programare
Primul meu program Python
Print statement
Comentarii
Variabile
Cele mai uzuale tipuri de date
Type casting
Intro in operatori
Input statement
"""

print("Hello Word, PYTA20!")
# print("Luni")
# print(29)
#comentam o linie de cod

# variabile
masina = "Volvo"          # date de tip string
an_inmatriculare = 2000   # date de tip int
pret_masina = 15000.50    # date de tip float
inmatriculata = True      # date de tip bool

# Mihai i-a cumparat o masina Volvo care este inmatriculata in anul 2000.
print(f"Mihai i-a cumparat o masina {masina} care este inmatriculata in anul {an_inmatriculare} ")
print(f"Pretul masinii a fost de {pret_masina} euro")
print("Pretul masinii a fost de {pret_masina} euro")

pret_masina = 10000.459
print(f"Pretul masinii este de {pret_masina} euro")
masina1 = "Dacia"
masina3 = "BMW"

nota_mate, nota_fizica, nota_sport = 10, 9, 7
print("nota mate: ", nota_mate)
print("nota fizica: ", nota_fizica)
print("nota sport: ", nota_sport)
ore_romana = ore_mate = 4

GRUPA = 'PYTA 20'
print(GRUPA)

nume = "Popescu"
prenume = 'Maria'
nume_restaurant = "Mc'Donalds"

#concatenarea stringurilor
nume_complet = nume + prenume
print(nume_complet)
varsta = 20
# Maria are 20 ani
print(f"{prenume} are {varsta} ani")
print(prenume + " are " + str(varsta) + "ani") # concatenam date de tip string si facem un type casting (convertim datele de tip int in date de tip string)

pret = "15"
print(type(pret))

pret = int(pret)
print(type(pret))

meniu = input("ce meniu doresti? ") # in variabila meniu salvam datele preluate de la tastura cu ajutorul functie input()
print(meniu) # afisam date din variabila meniu
print(type(meniu)) # afisam tipul de date

pret_meniu = int(input("care este pretul meniului? "))
print(pret_meniu)
print(type(pret_meniu))


# Maria a mers la Mc'Donalds si a cumparat un meniu mediu, iar pretul a fost de 15 lei
print(f"{prenume} a mers la {nume_restaurant} si a cumparat un meniu {meniu}, iar pretul a fost {pret_meniu} lei")

print(prenume + "a mers la " + nume_restaurant + " si a cumparat un meniu " + meniu + ", iar pretul a fost " + str(pret_meniu) + " lei")