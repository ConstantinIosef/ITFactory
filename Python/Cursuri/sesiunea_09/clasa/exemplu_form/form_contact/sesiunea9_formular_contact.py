"""
fa un formular dupa https://www.fundatiapascupas.ro/contact/
"""

class ContactFormular:
    def __init__(self, nume_prenume, email, telefon, mesaj):
        self.nume_prenume = nume_prenume
        self.email = email
        self.telefon = telefon
        self.proiect = [("la atelier","la atelier"), ("next steps", "next steps"), ("pasi impreuna", "pasi impreuna")]
        self.mesaj = mesaj

    def validare(self):

        #verificam daca toate campurile au fost completate
        if not all([self.nume_prenume, self.email, self.telefon, self.proiect, self.mesaj]):
            return False, "Toate campurile sunt obligatorii"
        else:
            return True, "Toate campurile au fost completate"

