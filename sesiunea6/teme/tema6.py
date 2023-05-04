# A. RECOMANDAT
# 1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva.

# B. OBLIGATORIU (MEDIU)

# ATENTIE!! Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati metodele clasei.

# 1. Clasa Cerc
# atribute: raza, culoare
# constructor pentru ambele atribute

# metode:
# descrie_cerc() -> va PRINTA culoarea si raza
# aria() -> va returna aria
# diametru()
# circumferinta()

import math

# class Cerc:
#
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f"Acest cerc are raza de {self.raza} cm si culoarea {self.culoare}")
#
#     def aria(self):
#         aria_cerc = self.raza * self.raza * math.pi
#         return aria_cerc
#
#     def diametru(self):
#         diametru_cerc = 2 * self.raza
#         return diametru_cerc
#
#     def circumferinta(self):
#         circumferinta = self.raza * 2 * math.pi
#         return circumferinta
#
#
# cerc1 = Cerc(2, 'rosu')
# print(cerc1)
# cerc1.descrie_cerc()
# print(cerc1.aria())
# print(cerc1.diametru())
# print(cerc1.circumferinta())
#
# cerc2 = Cerc(5, 'galben')
# print(cerc2)
# cerc2.descrie_cerc()
# print(cerc2.aria())
# print(cerc2.diametru())
# print(cerc2.circumferinta())


# 2. Clasa Dreptunghi

# atribute: lungime, latime, culoare
# constructor pentru toate atributele

# metode:
# descrie()
# arie()
# perimetru()
# schimba_culoare(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

# class Dreptunghi():
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie_dreptunghi(self):
#         print(f"Acest dreptunghi are lungimea de {self.lungime} cm, latimea de {self.latime} si culoarea {self.culoare}")
#
#     def aria_dreptunghi(self):
#         aria_dreptunghi = self.lungime * self.latime
#         return aria_dreptunghi
#
#     def perimetru_dreptunghi(self):
#         perimetru_dreptunghi = self.lungime * 2 + self.latime * 2
#         return perimetru_dreptunghi
#
#     def schimba_culoarea(self, noua_culoare):
#        self.culoare = noua_culoare
#        self.descrie_dreptunghi()
#
# dreptunghi1 = Dreptunghi(4, 2, 'galben')
# print(dreptunghi1)
# dreptunghi1.descrie_dreptunghi()
# print(dreptunghi1.aria_dreptunghi())
# print(dreptunghi1.perimetru_dreptunghi())
# dreptunghi1.schimba_culoarea('rosu')
#
# dreptunghi2 = Dreptunghi(10, 4, 'portocaliu')
# dreptunghi2.descrie_dreptunghi()
# print(dreptunghi2.aria_dreptunghi())
# print(dreptunghi2.perimetru_dreptunghi())
# dreptunghi2.schimba_culoarea('alb')


# 3. Clasa Angajat

# atribute: nume, prenume, salariu

# Connstructor pentru toate atributele

# Metodele:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

# class Angajat:
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f"Angajatul {self.nume} {self.prenume} are salariul de {self.salariu}")
#
#     def nume_complet(self):
#         nume_complet = self.nume + ' ' + self.prenume
#         return nume_complet
#
#     def salariu_lunar(self):
#         print(f"Salariul lunar al acestui angajat este {self.salariu}")
#
#     def salariu_anual(self):
#         salariu_anual = 12 * self.salariu
#         print(f"Salariul anual al acestui angajat este {salariu_anual}")
#
#     def marire_salariu(self, procent):
#         self.salariu = self.salariu + self.salariu * procent / 100
#         return self.salariu
#
#
# angajat1 = Angajat("Pop", "Maria", 10000)
# angajat1.descrie()
# print(angajat1.nume_complet())
# angajat1.salariu_lunar()
# angajat1.salariu_anual()
# print(angajat1.marire_salariu(25))
#
#
# angajat2 = Angajat("Pop", "Ion", 11000)
# angajat2.descrie()
# print(angajat2.nume_complet())
# angajat2.salariu_lunar()
# angajat2.salariu_anual()
# print(angajat2.marire_salariu(10))

# 4. Clasa Cont

# atribute: iban, titular_cont, sold

# constructor pentru toate

# metode:
# afisare_sold() -> Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare cont(suma)

class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.")

    def debitare_cont(self, suma):
        if suma <= self.sold:
            self.sold -= suma
        else:
            print("Fonduri insuficiente!")

    def creditare_cont(self, suma):
        self.sold += suma


cont1 = Cont('RO54BTRLRONCRT000000', 'Pop Ana', 20000)
cont1.afisare_sold()
print(cont1.sold)
cont1.debitare_cont(1000)
print(cont1.sold)
cont1.creditare_cont(1000)
print(cont1.sold)

cont2 = Cont('RO80BTRLRONCRT111111', 'Pop Alina', 500)
cont2.afisare_sold()
print(cont2.sold)
cont2.debitare_cont(4000)
print(cont2.sold)
cont2.creditare_cont(1000)
print(cont2.sold)


# BONUS (daca aveti timp soi doriti sa lucrati suplimentar)

# 5. Clasa Factura
# atribute: seria (va fi constanta, nu trebuie constructir, toate facturile vor avea aceeasi serie),
# numar, nume_produs, cantitate, pret_buc

# Constructor: toate atributele, fara serie

# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti

# Exemplu:
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | Cantitate | Pret Bucata | Total
# Telefon|     7     |    700      | 49000

# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

from datetime import date
from tabulate import tabulate


class Factura:
    seria = 123456

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def calc_total(self):
        return self.pret_buc * self.cantitate

    def genereaza_factura(self):
        print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, self.calc_total(), date.today()]],
                       headers=['Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data']))


factura1 = Factura(1, 'birou', 5.00, 100)
factura1.genereaza_factura()

factura2 = Factura(2, 'scaun', 3.00, 45)
factura2.schimba_cantitatea(4.00)
factura2.schimba_pretul(50)
factura2.schimba_nume_produs('scaun de masaj')
factura2.genereaza_factura()

# 6. Clasa Masina
# atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set),
# inmatriculata (bool)

# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# culori_disponibile = alegeti 5-7 culori
# marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# inmatriculata = False

# constructor: model, viteza_maxima

# Metode:
# descrie() (se vor printa toate atributele, in afara de culori disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vospeste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare este in culori_disponibile,
# altfel afisati un mesaj.
# accelereaza(viteza) - se va accelera la o anumita viteza, daca viteza e negativa - mesaj de eroare,
# daca viteza e mai mare decat viteza maxima - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0

class Masina:
    marca = 'Dacia'
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = ['rosu', 'verde', 'alb', 'albastru', 'portocaliu', 'negru', 'galben']
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Marca masinii este: {self.marca}')
        print(f'Modelul masinii este: {self.model}')
        print(f'Viteza maxima a masinii este: {self.viteza_maxima}')
        print(f'Viteza actuala a masinii este: {self.viteza_actuala}')
        print(f'Culoarea masinii este: {self.culoare}')
        print(f'Masina este inamtriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopseste_masina(self, noua_culoare):
        if noua_culoare in self.culori_disponibile:
            self.culoare = noua_culoare
            print(f'Noua culoare a masinii este: {self.culoare}')
        else:
            print('Culoarea aleasa de dvs nu este in paletarul nostru.')

    def accelereaza(self, viteza_dorita):
        if viteza_dorita < 0:
            print('EROARE!')
        elif viteza_dorita >= self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza_dorita
        print(f'Viteza actuala este: {self.viteza_actuala}')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Viteza actuala este: {self.viteza_actuala}. Am oprit masina.')

# 7. Clas ToDoList

# Atribute: to_do (dict, chiea e numele task-ului, valoarea e descrierea)
# La inceput nu avem task-uri, dict e gol si nu avem nevoie de constructor.

# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizeaza_task(nume) - se va sterge din dict
# afiseaza_todo_list() - afiseaza doar cheile
# afiseaza_detalii_suplimentare(nume_task) = in functie de numele task-ului, printam
# detalii suplimentare. Daca task-ul nu e in to_do list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# Daca raspunde da - ii cerem detalii task si salvam nume + detalii in dict

class ToDoList:
    to_do = {}

    def adauga_task(self, nume_task, descriere_task):
        self.to_do[nume_task] = descriere_task
        print('Am adaugat taskul cu succes')

    def finalizeaza_task(self, nume_task):
        del self.to_do[nume_task]

    def afiseaza_todo_list(self):
        print(f'Task-urile din TODO sunt: {self.to_do.keys()}')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.to_do:
            print(f'Detalii pt taskul {nume_task}: {self.to_do[nume_task]}')
        else:
            print('Nu am gasit taskul dorit')
            raspuns = input('Vrei sa adaugi task ul in lista?')
            if raspuns.lower() == 'da':
                descriere_task = input('Introdu descrierea pentru noul task: ')
                self.to_do[nume_task] = descriere_task
                print('Am adaugat taskul cu succes')
            elif raspuns.lower() == 'nu':
                print('La revedere!')