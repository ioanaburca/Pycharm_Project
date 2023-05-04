# USOR - recomandat
# 1. Revizualizeaza intalnirea 4 si ia notite in caz ca ti-a scapat ceva.
# 2. Vizualizeaza video despre Flow Control din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 5 despre Functii din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
import random

# TEMA OBLIGATORIE - nivel usor spre mediu
# SETS
# 1. Se dau urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata'}
weekend = {'sambata', 'duminica'}

# a. Incearca sa adaugi in setul zile_sapt, ziua de 'duminica'.
# zile_sapt.add('duminica')
# print(zile_sapt)

# Ce observi? Scrie intr-un comentariu observatiile tale.
#  a fost adaugata si ziua de duminica

# b. Foloseste un IF si verifica DACA:
# - weekend este un subset al zilelor din saptamana (adica daca elementele din setul weekend se regasesc
# intre elementele din setul zile_sapt)
# - weekend nu este un subset din setul zile_sapt
# Salveaza rezultatul pentru fiecare caz intr-o variabila bool si afiseaz-o intr-un mesaj sugestiv.

# este_subset = None
# if weekend.issubset(zile_sapt):
#     este_subset = True
#     print(f"{este_subset} -> weekend este subset al set-ului zile_sapt")
# else:
#     este_subset = False
#     print(f"{este_subset} -> weekend NU este subset al set-ului zile_sapt")

# c. Afiseaza diferentele intre cele doua seturi (adica elementele care sunt in zile_sapt
# si nu sunt in weekend si invers).
# print(zile_sapt.difference(weekend))
# print(weekend.difference(zile_sapt))

# d. Afiseaza intersectia elementelor din cele doua seturi (adica elementele care exista in ambele seturi).
# print(zile_sapt.intersection(weekend))

# TUPLES
# 2. Calcularea valorii totale a unui cos de cumparaturi
# Un client a cumparat mai multe articole dintr-un magazin si dorim sa calculam valoarea totala a cosului
# de cumparaturi.
# Citeste de la tastatura numele si pretul pentru trei articole, pe rand.
# Salveaza numele si pretul pentru fiecare articol intr-un tuplu. (Astfel vei avea trei tupluri).
# Calculeaza pretul total platit de client si afiseaza rezultatul intr-un mesaj sugestiv.
# numele_produs1 = input('Introdu numele produsului: ')
# pret_produs1 = float(input('Introdu pretul produsului: '))
#
# numele_produs2 = input('Introdu numele produsului: ')
# pret_produs2 = float(input('Introdu pretul produsului: '))
#
# numele_produs3 = input('Introdu numele produsului: ')
# pret_produs3 = float(input('Introdu pretul produsului: '))
#
# produs1 = (numele_produs1, pret_produs1)
# produs2 = (numele_produs2, pret_produs2)
# produs3 = (numele_produs3, pret_produs3)
#
# pret_total = produs1[1] + produs2[1] + produs3[1]
# print(f'Pretul total pentru cumparaturi este: ', {pret_total})


# 3. Se dau urmatoarele tupluri care caracterizeaza tipul de forma geometrica si lungimile laturilor sale.
# forma_1 = ("Patrat", 5)
# forma_2 = ("Dreptunghi", 2, 3)
#
# # Calculeaza perimetrul si aria pentru fiecare forma geometrica
# perimetru_forma_1 = forma_1[1] * 4
# print('Perimetrul patratului este', perimetru_forma_1)
# aria_forma_1 = forma_1[1] * forma_1[1]
# print('Aria patratului este', aria_forma_1)
#
# perimetru_forma_2 = (forma_2[1] * 2) + (forma_2[2] * 2)
# print('Perimetrul dreptunghiului este', perimetru_forma_2)
# aria_forma_2 = forma_2[1] * forma_2[2]
# print('Aria dreptunghiului este', aria_forma_2)


# 4. Citeste de la tastatura notele obtinute de un student la cele 4 examene date in sesiune.
# Salveaza notele intr-un tuplu.
# Calculeaza media studentului la finalul sesiunii.
# nota1 = float(input('Introdu nota examen 1: '))
# nota2 = float(input('Introdu nota examen 2: '))
# nota3 = float(input('Introdu nota examen 3: '))
# nota4 = float(input('Introdu nota examen 4: '))
#
# note_examene = (nota1, nota2, nota3, nota4)
# print(note_examene)
#
# media = sum(note_examene) / len(note_examene)
# print(media)

# Daca media este intre 8-10 (inclusiv capetele de interval), afiseaza-i un mesajul utilizatorului
# si spune-i ca s-a descurcat foarte bine.
# Daca media este intre 5-8, afiseaza-i un mesaj utilizatorului sa se ambitioneze
# sesiunea urmatoare si sa invete mai mult ca sa obtina bursa.
# Daca media este sub 5, afiseaza-i utilizatorului un mesaj in care sa ii spui sa nu isi faca planuri pe vara ca il
# asteapta sesiunea de restante.

# if media >= 8 and media <= 10:
#     print('Media ta este', media, 'Te-ai descurcat foarte bine!')
# elif media >=5 and media <= 8:
#     print('Media ta este' , media, 'Poti mai mult!')
# elif media < 5:
#     print('Media ta este', media, 'Nu ai trecut examenul!')
# else:
#     print('Ne vedem la vara!')

# CONDITII REPETITIVE

# 5. Se da lista:
# masini = ['Audi', 'Volvo', 'Dacia', 'Mercedes', 'Fiat', 'Trabant', 'Lastun']

# a. Folosind un for si lungimea listei, itereaza prin lista si pentru fiecare element
# afiseaza mesajul 'Masina mea preferata este x', unde x este masina.
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')

# b. Faceti acelasi lucru folosind un for each.
# for i in masini:
#     print(f'Masina mea preferata este {i}')

# c. Faceti acelasi lucru folosind un while.
# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1

# 6. Folosind lista de la exercitiul 5, modifica elementele din lista astfel incat sa fie scrise cu majuscule,
# exceptand primul si ultimul element din lista.
# Printati varianta finala a listei.
# for i in range(1, (len(masini)-1)):
#     masini[i] = masini[i].upper()
#
# print(masini)


# 7. Folosind lista de la exercitiul 5:
# Vine un cumparator care vrea sa cumpere un Mercedes.
# Itereaza prin lista cu for each, verifica daca masina e mercedes.
# Daca da, afiseaza mesajul
# "Am gasit masina dorita de dumneavoastra" si iesim din ciclu folosind un cuvant cheie care face acest lucru.
# Daca nu, afiseaza "Am gasit masina X. Mai cautam."
# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dumneavoastra')
#         break
#     print('Am gasit masina', {masina}, 'Mai cautam')


# 8. Folosind lista de la exercitiul 5:
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#   Folositi un cuvant cheie care sa dea skip la ce urmeaza
# In celalalte cazuri, printati mesajul "S-ar putea sa va placa masina x.".
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     print('S-ar putea sa va placa masina', masina)


# 9. Modernizati parcul de masini.
# Creati o lista goala, masini_vechi.
# Iterati prin masini. (lista de la exercitiul 5)
# Cand gasiti Lastun sau Trabant:
#   Salvati aceste masini in masini_vechi.
#   Suprascrieti cu 'Tesla' (in lista initiala de masini)
# Printati: "Modele vechi: x"
# Printati: "Modele noi: y"
# masini_vechi = []
# for i in  range(0, len(masini)):
#     if masini[i] in ['Lastun', 'Trabant']:
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
#
# print(f"Modele vechi: {masini_vechi}")
# print(f"Modele noi: {masini}")


# 10. Avand dictionarul:
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu bugetul de 15 000 euro.
# Prezentati doar masinile care se incadreaza in acest buget:
# Iterati prin dict.items() si accesati masina si pretul.
# Printati "Pentru un buget de sub 15 000 euro puteti alege masina x"
# buget = 15000
# for masina, pret in pret_masini.items():
#     if pret < buget:
#         print(f'Pentru un buget de sub 15 000 euro puteti alege masina {masina}')
#

# 11. Avand lista:
# numere = [5, 7, 9, 3, 3, 1, 0, -4, 3]
# Afisati de cate ori apare 3. (! NU aveti voie sa folositi metoda count()!)
# i = 0
# for i in numere:
#     if i == 3:
#         print(f'Numarul 3 aparare de {i} ori')
#         i += 1

# 12. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin lista si calculati suma numerelor din lista.
# ! NU aveti voie sa folositi functia sum()!
# suma = 0
# for numar in numere:
#     suma += numar
# print(f'Suma numerelor este: {suma}')

# 13. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin lista si afisati cel mai mare numar.
# ! NU aveti voie sa folositi functia max()!
# nr_mare = 0
# for numar in numere:
#     if numar > nr_mare:
#         nr_mare = numar
# print(f'Numarul cel mare este: {nr_mare}')

# 14. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin ea
# - daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa.
# Exemplu: Daca e 3, sa devina -3.
# Afisati noua lista.

# for index in range(0, len(numere)):
#     if numere[index] > 0:
#         numere[index] = -1 * numere[index]
#
# print(f"Noua lista arata asa: {numere}")


# # TEMA OPTIONALA - DE GRUP (MAY NEED GOOGLE)

# 1. Se dau listele:
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Populati corect listele goale pe baza elementelor din lista alte_numere.
# Afisati cele 4 liste la final.
# for numere in alte_numere:
#     if numere > 0:
#         numere_pozitive.append(numere)
#     else:
#         numere_negative.append(numere)
#     if numere % 2 == 0:
#         numere_pare.append(numere)
#     else:
#         numere_impare.append(numere)
#
# print(numere_pozitive)
# print(numere_negative)
# print(numere_pare)
# print(numere_impare)



# 2. Folosind lista alte_numere de la exercitiul anterior:
# Ordonati lista crescator, fara sa folositi sort.
# Va puteti inspira vizual de aici: https://www.youtube.com/watch?v=lyZQPjUT5B4
# for i in range(len(alte_numere)):
#     for j in range(i + 1, len(alte_numere)):
#
#         if alte_numere[i] > alte_numere[j]:
#             alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
# print(alte_numere)

# 3. Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# numar_ghicit = None
# Folosind un while:
#   User-ul introduce un numar
#   Programul ii spune:
#   Numarul secret e mai mare
#   Numarul secret e mai mic
#   Ai ghicit.
# Daca utilizatorul a ghicit, while-ul trebuie sa se opreasca!
# numar_secret = random.randint(1, 30)
# print(numar_secret)
# numar_ghicit = None
# while numar_ghicit != numar_secret:
#     numar_ghicit = int(input('Introdu un numar: '))
#     if numar_ghicit < numar_secret:
#         print('Numarul secret este mai mic ')
#     elif numar_ghicit > numar_secret:
#         print('Numarul secret este mai mare ')
# else:
#     numar_ghicit = numar_secret
#     print('Ai ghicit')

# 4. Alegeti un numar de la tastatura si generati o piramida, conform exemplului:
# Daca utilizatorul va introduce numarul 7, se va genera/ afisa urmatoarea piramida:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# nr = int(input('Alege un numar:'))
# for i in range(1, nr + 1):
#     print(str(i)*i)

# 5.
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# Iterati prin lista 2d.
# Printati "Cifra curenta este x"
# (HINT: nested for - adica for in for)
for lista_cifre in tastatura_telefon:
    for cifre in lista_cifre:
        print(f'Cifra curenta este', {cifre})

