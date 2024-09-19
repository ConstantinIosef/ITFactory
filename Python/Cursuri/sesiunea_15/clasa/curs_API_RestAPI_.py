""""HTTP, API - Exemple practice"""

import requests

url = "https://dummyjson.com/products"

response = requests.get(url=url)
print(response.status_code)

# print(response.text)
dict_products = response.json()
for index in range(0, 3):
    print(f'ID PRODUS:{dict_products["products"][index]["id"]}'
          f'NUME PRODUS: {dict_products["products"][index]["title"]},'
          f'PRET PRODUS: {dict_products["products"][index]["price"]}')

produse_ramase = len(dict_products["products"]) - 3
print(f"Avem {produse_ramase} de produse care nu au fost afisate")

# GET product by id
id = 20
response_get_product_by_id = requests.get(f"https://dummyjson.com/products/{id}")
produs = response_get_product_by_id.json()

# print(produs)
print(f"ID PRODUS:{produs['id']}, Nume: {produs['title']}")

print("---" * 50)
#Metoda HTTP POST - o folosim pt a trimite date catre server

json_data = {
    "title": "Produs nou"
}

response = requests.post(url="https://dummyjson.com/products/add", json=json_data)
print(response.status_code)
print(response.json())

## Metodele HTTP PUT & PATCH - le folosim pt a actualiza date
# Metoda HTTP PUT - o folosim cand vrem sa facem o actualizare completa
print("---" * 50)
json_data = {
    "title": "Titlu nou",
    "price": 203.23
}
response = requests.put(url="https://dummyjson.com/products/3", json=json_data)
print(response.status_code)
print(response.json())

#Metoda PATCH - o folosim cand vrem sa facem o actualizare partiala
print("---" * 50)
json_data = {
    "title": "Titlu nou nou",
}
response = requests.patch(url="https://dummyjson.com/products/3", json=json_data)
print(response.status_code)
print(response.json())

# Metoda HTTP DELETE - o folosim cand vrem sa stergem anumite date
print("---" * 50)
response = requests.delete(url="https://dummyjson.com/products/20")
print(response.json())

# GET all products skip & limit
print("---" * 50)
param = {
    "limit": 15,
    "skip": 5
}

response = requests.get(url=url, params=param)

if response.status_code == 200:
    produse = response.json()
    print(produse)
else:
    print(f'Eroare: {response.status_code}', {response.text})

# GET search product
print("---" * 50)
param = {
    "q": "phone",
    "limit": 5
}

url_search = "https://dummyjson.com/products/search"

response = requests.get(url=url_search, params=param)

if response.status_code == 200:
    produse = response.json()
    print(produse)
else:
    print(f'Eroare: {response.status_code}, {response.text}')