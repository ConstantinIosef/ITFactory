"""
EX1: Se da numarul x = -5.
Foloseste un while pentru a afisa numerele negative pornind
de la -5.
La final, afiseaza un mesaj ca s-au afisat toate numerele
negative.
"""

print("rezolvare ex 1.")
x = -5

while x < 0:    # x = -5, x = -4, x = -3, x = -2, x = -1, x = 0
    print(x)    # -5, -4, -3, -2, -1
    x += 1      # x= -5 + 1 , x = -4 + 1, x = -3 + 1, x = -2 +1, x = -1+1
print("S-au afisat toate numerele negative ")


"""
EX2: Calcularea mediei
Ne dorim sa cerem utilizatorului sa introduca notele
luate la examene. 
Vom lua input-ul de la utilizator, pana
cand acesta introduce -1.
In functie de notele luate, trebuie sa calculam media aritmetica
si sa o afisam.
"""
print("rezolvare ex 2.")
note_utilizator = []
nota_utilizator = 0

# while nota_utilizator != -1:
#     nota_utilizator = int(input("Introdu nota: "))
#     if nota_utilizator > 0 and nota_utilizator <= 10:
#         note_utilizator.append(nota_utilizator)
#
# print(note_utilizator)
#
# if len(note_utilizator) != 0:
#     media = sum(note_utilizator)/len(note_utilizator)
#     print("media aritmetica este:", media)
# else:
#     print("Nu avem note introduse")

"""
EX3: Afiseaza toate numerele pare pana la 10.
"""
print("rezolvare ex 3.")

for numar in range(2, 10, 2):
    print(numar)


"""
EX4: Se da lista:
legume = ['spanac', 'castraveti', 'conopida', 'ardei']
Afiseaza toate elementele din lista accesandu-le dupa index.
"""
print("rezolvare ex 4.")
legume = ['spanac', 'castraveti', 'conopida', 'ardei']
# lungime_lista = len(legume)
# for i in range(lungime_lista):

for i in range(len(legume)):
    print(legume[i])

"""
EX5:
2. Se da lista:
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
Sa se afiseze toate produsele care au pretul mai mare de 5 lei.
"""
print("rezolvare ex 5.")
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]

for produs in produse:
    # print(produs)
    if "pret" in produs.keys() and produs["pret"] > 5:
        print(produs["nume produs"])



