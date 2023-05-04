# RECAPITULARE

# SETURI
# 1. Explica intr-un comentariu:

# a. Ce sunt seturile
# SETURILE sunt structuri de date care contin elemente UNICE.
# my_set = {1, 2, 3}

# b. Sunt seturile ORDONATE/NEORDONATE?
# Seturile sunt NEORDONATE => Elementele nu sunt salvate in memorie
# in ordinea in care sunt adaugate + nu pot fi accesate dupa index.

# c. Sunt seturile MUTABILE/IMUTABILE?
# Seturile sunt MUTABILE => putem sterge sau adauga elemente

# 2. Se da setul:
# fructe = {'capsuni', 'mere', 'pere'}

# a. Adauga un nou element in set: 'pepene'.
# fructe.add('pepene')
# print(fructe)

# b. Adauga 'capsuni' in set. Ce observi?
# fructe.add('capsuni')
# print(fructe)

# c. Sterge elementul 'capsuni'.
# fructe.remove('capsuni')
# print(fructe)

# d. Sterge un element aleator.
# fructe.pop()
# print(fructe)

# e. Salveaza dimensiunea set-ului intr-o variabila si afiseaz-o.
# x = len(fructe)
# print(x)

# TUPLURI
# 1. Explica intr-un comentariu:

# a. Ce sunt tuplurile
# Tuplurile sunt structuri de date care pastreaza mai multe valori/elemente.
# my_tuple = ('a', 'b', 'c')

# b. Sunt tuplurile ORDONATE/NEORDONATE?
# Tupluri = ORDONATE => elementele pot fi accesate dupa index +
# se salveaza in memorie in aceeasi ordine in care sunt adaugate

# c. Sunt tuplurile MUTABILE/IMUTABILE
# Tupluri = IMUTABILE -> elementele nu se pot modifica

# 2. Citeste de la tastatura numele a trei tari pe rand.
# Salveaza numele celor trei tari intr-un tuplu.
# Folosind un for, afiseaza urmatorul mesaj pentru fiecare tara:
# Tara mea preferata este x.

# tara1 = input("Tara 1: ")
# tara2 = input("Tara 2: ")
# tara3 = input("Tara 3: ")
#
# tari = (tara1, tara2, tara3)
#
# for i in tari:
#     print("Tara mea preferata este ", i)

# WHILE
# 1. Explica intr-un comentariu ce este un while.
# WHILE = ciclu repetitiv care se va executa atata timp cat o
# conditie (conditia data la while) este adevarata.

# While-ul poate avea si un ELSE. Codul din ELSE, se va executa
# mereu, dupa ce while-ul ajunge la final.

# 2. Mihai doreste sa isi cumpere o bicicleta electrica.
# Aceasta costa 10 000 lei si ar vrea sa stie cate luni va dura
# sa stranga suma dorita daca economiseste 1 000 lei in fiecare luna.

# buget = 0
# luni = 0
#
# while buget < 10000:
#     luni += 1
#     buget += 1000
# else:
#     print(luni)

# FOR
# 1. Explica intr-un comentariu ce este un for.

# FOR = ciclu repetitiv prin care putem da instructiuni pentru
# fiecare element dintr-un iterabil/dintr-o structura de date.

# my_list = ['a', 'b', 'c']
# for i in my_list:
#     print(i)
#     # if i == 'b':
#     #     break
# else:
#     print("Hello")

# 2. Explica verbal ce face urmatoarele programe:

# a.
# fructe = ['capsuni', 'mere', 'pere']
# for fruct in fructe:
#     if fruct == 'capsuni':
#         print("Am gasit fructul meu preferat")
#         break
#     print(f"Acesta este un fruct bun, dar nu preferatul meu {fruct}")


# b.
# lista_numere = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_div_5 = []
# for i in lista_numere:
#     if i % 5 == 0:
#         lista_div_5.append(i)
#
# print(lista_div_5)

# 3. Se da lista:
my_list = [4, 56, 24, 70, 5, 3, 53, 22]

# Folosind lista data, va trebui folositi un for, sa ajungi
# la urmatoarea lista pe care sa o si afisezi:
# [0, 0, 0, 0, 5, 3, 53, 0]
#
# Rezolva problema folosind for. Apoi rezolva aceeasi problema
# folosind foreach

# for
# for i in range(len(my_list)):
#     if my_list[i] % 2 == 0:
#         my_list[i] = 0
# print(my_list)

# foreach
# for i in my_list:
#     if i % 2 == 0:
#         i = 0
#
# print(my_list)