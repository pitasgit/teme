from math import pi
import random


# Clasa Cerc Atribute: raza, culoare Constructor pentru ambele atribute Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()


class Cerc:

    raza = None
    Culoare = None

    def __init__(self):
        self.raza = int(input("introduce raza: "))
        self.culoare = str(input("introduce culoarea: "))

    def descrie_cerc(self):
        print("Raza este " + str(self.raza) + " iar culoarea este " + self.culoare)

    def aria(self):
        aria = pi*(self.raza*self.raza)
        return print(f"Aria este {aria}")

    def diametru(self):
        diametru = (self.raza + self.raza)
        return print(f"Diametrul este {diametru}")

    def circumferinta(self):
        circumferinta = 2 * pi * self.raza
        return print(f"Circumferinta este {circumferinta}")


cerc2 = Cerc()
cerc2.descrie_cerc()
cerc2.aria()
cerc2.diametru()
cerc2.circumferinta()
print("----------------------------")

# Clasa Dreptunghi Atribute: lungime, latime, culoare
# Constructor pentru toate atributele Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().


class Dreptunghi:
    lungime = None
    latime = None
    culoare_dreptunghi = None

    def __init__(self):
        self.lungime = int(input("va rugam introduceti o valoare a lungimii: "))
        self.latime = int(input("va rugam introduceti o valoare a latimii: "))
        self.culoare_dreptunghi = str(input("va rugam introduceti o culoare: "))

    def descrie_dreptunghi(self):
        return print("Dreptunghiul are lungimea " + str(self.lungime) + ", " + "latimea " + str(
            self.latime) + " iar culoarea acestuia este " + str(self.culoare_dreptunghi) + ".")

    def ariad(self):
        aria_dreptunghi = self.lungime * self.latime
        return print("Aria dreptunghiului este " + str(aria_dreptunghi))

    def perimetruld(self):
        perimetruld = str(self.lungime * 2 + self.latime * 2)
        print("Perimetrul este " + perimetruld)
        return perimetruld

    # nu inteleg care varianta e mai buna, daca am returnat corect, sau trebuia sa returnez print din prima?

    def schimba_culoarea(self, noua_culoare):
        self.culoare_dreptunghi = noua_culoare
        if self.culoare_dreptunghi == "Verde":
            print(f"Noua culoare este {self.culoare_dreptunghi}")


dreptunghi1 = Dreptunghi()
dreptunghi1.descrie_dreptunghi()
dreptunghi1.ariad()
dreptunghi1.perimetruld()
dreptunghi1.schimba_culoarea(noua_culoare="Verde")
dreptunghi1.descrie_dreptunghi()
print("----------------------------")


class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self):
        self.nume = str(input("Introduceti numele: "))
        self.prenume = str(input("introduceti prenumele: "))
        self.salariu = int(input("introduceti salariul: "))

    def descrie_angajat(self):
        print(f"Angajatul se numeste {self.nume} {self.prenume} si are un salariu de {self.salariu}")

    def nume_complet(self):
        nume_complet = self.nume + " " + self.prenume
        return print(f"numele cumplet este {nume_complet}")

    def salariu_lunar(self):
        salariu_lunar = self.salariu
        print(f"Salariul lunar este {salariu_lunar}")
        return salariu_lunar

    # nu am inteles de ce trebuie sa trec de ori salariul si salariul lunar. trebuie cumva sa ma folosesc de el
    # pentru definirea salariului anual? daca da, cum?

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f"Salariul anual este {salariu_anual}")
        return salariu_anual

    def marire_salariu(self):
        procent = int(input("introduceti un procent: ")) / 100
        marire = (self.salariu * procent) + self.salariu
        print(f"Noul salariu este {marire}")
        return procent


angajat = Angajat()
angajat.descrie_angajat()
angajat.salariu_lunar()
angajat.nume_complet()
angajat.salariu_anual()
angajat.marire_salariu()
print("----------------------------")


# 4.Clasa Cont Atribute: iban, titular_cont, sold Constructor pentru toate atributele Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)


class Cont:
    iban = None
    titular_cont = None
    sold = None
    user_choice = None

    def __init__(self):
        self.iban = str(input("Introduceti IBAN: "))
        self.titular_cont = str(input("Introduceti numele titularului: "))
        self.sold = random.randint(0, 1000)

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de: {self.sold} RON")

    def debitare_cont(self):
        suma_debit = int(input("Va rugam introduceti suma dorita: "))
        debitare = self.sold - suma_debit
        if debitare < 0:
            print("Fonduri insuficiente")
        else:
            print("Tranzactie acceptata")
            print(f"Mai aveti in cont {debitare} RON")
        return

    def creditare_cont(self):
        suma_credit = int(input("Va rugam introduceti suma de adaugat: "))
        creditare = self.sold + suma_credit
        if suma_credit == 0:
            print("Va multumim pentru folosirea serviciilor noastre")
        elif suma_credit > 0:
            print(f"aveti in cont {creditare}")
        return


cont1 = Cont()
cont1.afisare_sold()
cont1.debitare_cont()
cont1.creditare_cont()
print("-------Am incercat sa fac cu user choice, debitare sau creditare dar nu mi-a iesit-------------------")
