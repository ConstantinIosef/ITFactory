from sesiunea9_formular_contact import ContactFormular

def main():
    nume_prenume = input("Introdu numele: \n")
    email = input("Introdu emailul: \n")
    telefon = input("Introdu telefonul: \n")
    mesaj = input("Introdu mesaj \n")
    formContact = ContactFormular(nume_prenume, email, telefon, mesaj)

    print("Alege proiectul in care vrei sa te implici: ")
    for i,(proiect, proiect_ales) in enumerate(formContact.proiect):
        print(f"{i+1}, {proiect_ales}")


    while True:
        try:
            nr_proiect = int(input(f"Scrie numarul proiectului ales: \n"))
            if 1 <= nr_proiect <= len(formContact.proiect):
                formContact.proiect = formContact.proiect[nr_proiect - 1][0]
                break
            else:
                print("Numarul introdus nu este valid")
        except ValueError:
            print("Te rugam sa introduci un numar astfel incat sa stim care este proiectul in care vrei sa te implici")

    # validam si trimitem formularul completat
    formular_valid, mesaj = formContact.validare()
    if formular_valid:
        print("Mesajul a fost trimis")
    else:
        print("eroare:", mesaj)


main()