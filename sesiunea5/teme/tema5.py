# a. USOR (RECOMANDAT)
# 1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/

# b. OBLIGATORIU: USOR SPRE MEDIU

# IMPORTANT! -> Pentru TOATE EXERCITIILE, apelati functia de cel putin 2 ori cu valori
# diferite pentru a testa. Daca functia are return, printati raspunsul!

# 1. Scrie o functie care sa calculeze si sa returneze suma a 2 numere
# def suma_numere(a, b):
#     suma = a + b
#     return suma
#
# rezultat = suma_numere(2, 5)
# print(rezultat)

# # 2. Scrie o functie care sa returneze True daca un numar este par, False daca este impar
# def este_par(i):
#     if i % 2 == 0:
#         return True
#     else:
#         return False
#
# print(este_par(7))
# print(este_par(2))
#
# # 3. Scrie o functie care sa returneze numarul total de caractere din numele tau complet
# # (nume, prenume, nume_mijlociu)
# def nr_caractere(nume, prenume, nume_mijlociu):
#     nume_complet = nume + prenume +nume_mijlociu
#     return len(nume_complet)
#
# print(nr_caractere('Burca', 'Ioana', 'Andreea'))

# # 4. Scrie o functie care returneaza aria dreptunghiului
# def aria_dreptunghiului(a, b):
#     aria = a * b
#     return aria
#
# print(aria_dreptunghiului(4, 2))
#
# # 5. Scrie o functie care returneaza aria cercului
# def aria_cercului(i):
#     aria = i ** 2
#     return aria
#
# print(aria_cercului(2))

# a doua varianta de rezolvare
# def get_circle_area(r):
#     import math
#
#     return math.pi * r ** 2
#
#
# area1 = get_circle_area(2)
# area2 = get_circle_area(4)
#
# print(area1)
# print(area2)

# 6. Scrie o functie care returneaza True daca un caracter x se gaseste intr-un string dat, False daca nu.
# def gaseste_caracter(x,  string):
#    if x in string:
#     return True
#    else:
#     return False
#
# print(gaseste_caracter('l', 'Lalelelor'))


# 7. Scrie o functie fara return care primeste ca parametru un string si printeaza pe ecran:
# - Nr. caractere lower case este x
# - Nr. caractere upper case este y
# def print_lower_and_upper_chars(sequence):
#     chars = {
#         'lower': 0,
#         'upper': 0
#     }
#     for char in sequence:
#         if char.islower():
#             chars['lower'] += 1
#         elif char.isupper():
#             chars['upper'] += 1
#
#     print(f"Number of lowercase letters: {chars['lower']}")
#     print(f"Number of uppercase letters: {chars['upper']}")
#
#
# print_lower_and_upper_chars('aabbCCDD')
# print_lower_and_upper_chars('aaa')
# print_lower_and_upper_chars('ABCD')
# print_lower_and_upper_chars('123')

# 8. Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele pozitive.
# def lista_numere(lista):
#     nr_pozitive = [];
#     for numar in lista:
#         if numar >= 0:
#             nr_pozitive.append(numar)
#
#     return nr_pozitive
# lista = [1, -1, 2, -13, 14]
# print(lista_numere(lista))





# 9. Scrie o functie care nu returneaza nimic. Primeste 2 numere si printeaza:
# - primul numar x este mai mare decat al doilea y
# - al doilea numar y este mai mare decat primul numar x
# - Numerele sunt egale.
# def comparatie_numere(x, y):
#     if x > y:
#         print(f' {x}  este mai mare ca {y}')
#     elif y > x:
#         print(f' {y}  este mai mare ca {x}')
#     else:
#         print('Numerele sunt egale.')
#
# comparatie_numere(2, 4)
# comparatie_numere(4, 4)


# 10. Scrie o functie care primeste un numar si un set de numere.
# Printeaza 'am adaugat numarul nou in set' + returneaza True
# sau printeaza 'Nu am adaugat numarul nou in set. Acesta exista deja' + returneaza False
# def adauga_numere(numar, set_numere):
#     if numar in set_numere:
#         print('Nu am adaugat nr nou in set. Acesta exista deja')
#         return False
#     else:
#         print('am adaugat numarul nou in set')
#         set_numere.append(numar)
#         return set_numere
# lista_numere = adauga_numere(2, [2, 4, 5])
# print(lista_numere)

# c. OPTIONALE (STUDIU DE ECHIPA) -> may need google

# 1. Scrie o functie care primeste o luna din an si returneaza cate zile are acea luna.
# def luna_an(luna):
#     dict = {
#         1: '31',
#         2: '28',
#         3: '30',
#         4: '31',
#         5: '30',
#         6: '31',
#         7: '30',
#         8: '31',
#         9: '30',
#         10: '31',
#         11: '30',
#         12: '31',
#     }
#     print(f'Luna {luna} are {dict[luna]}')
#
# luna_an(2)
# luna_an(5)

# 2. Scrie o functie calculator care sa returneze 4 valori: suma, diferenta, inmultirea a 2 numere.
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
# def calculator (a, b):
#     suma = a + b
#     diferenta = a - b
#     inmultirea = a * b
#     impartirea = a / b
#     return suma, diferenta, inmultirea, impartirea
#
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)



# 3. Scrie o functie care primeste o lista cu cifre (adica doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un dictionar care ne spune de cate ori apare fiecare cifra
# =>
# dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
# def lista_cifre(lista):
#     dict = {}
#     for numar in lista:
#         dict[numar] = lista.count(numar)
#     return dict
#
# lista = [1, 5, 4, 8, 4, 1 ,2]
# print(lista_cifre(lista))

# 4. Scrie o functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
#
# def get_max(a, b, c):
#     numbers = [a, b, c]
#     return max(numbers)
#
#
# print(get_max(1, 2, 3))
# print(get_max(5, 200, -300))

# 5. Scrie o functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3, suma va fi 6 (0 + 1 + 2 + 3)

# def get_sum(a):
#     result = 0
#     for i in range(0, a + 1):
#         result = result + i
#
#     return result
#
#
# print(get_sum(3))
# print(get_sum(2))
# print(get_sum(5))


# 6. Scrie o functie care primeste 2 liste de numere (numerele pot fi dublate).
# Returnati valorile comune

# exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}

# def get_common_values(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     return set1.intersection(set2)
#
# print(get_common_values([1,5,1,4], [5,1,2,8]))
# print(get_common_values([7,10,5,5,9], [10,1,5,9,4]))

# 7. Scrie o functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10 %, pretul va fi 90.
# Tratati cazurile in care reducerea este invalida. De exemplu o reducere de 110 % e invalida.

# def apply_discount(price, discount):
#     if 0 < discount <= 100:
#         return price - price * discount / 100
#     else:
#         return 0
#
#
# print(apply_discount(100, 10))
# print(apply_discount(100, 120))

# 8. Scrie o functie care sa afiseze dara si ora curenta din RO.
# (bonus: afisati si data si ora curenta din China)

# import pytz
# import datetime
#
# def get_current_datetime(timezone):
#     tz = pytz.timezone(timezone)
#     current_datetime = datetime.datetime.now(tz)
#     print(current_datetime)
#
# # print(pytz.all_timezones)
# get_current_datetime('Europe/Bucharest')
# get_current_datetime('Asia/Shanghai')


# 9. Scrie o functie care sa afiseze cate zile mai sunt pana la ziua ta/ sau pana la craciun daca nu vrei sa ne zici
# cand e ziua ta :D.

def countdown(day, month, year):
    import datetime

    data_curenta = datetime.date.today()
    data_dorita = datetime.date(year, month, day)
    if year < data_curenta.year:
        data_dorita = datetime.date(data_curenta.year, month, day)
    zile_ramase = (data_dorita - data_curenta).days
    print(f'Mai sunt {zile_ramase} zile pana la eveniment!')


countdown(25, 12, 2023)
countdown(29, 6, 1996)

def suma(a,b): #defineste functia suma cu 2 parametri
    suma = a + b  #calcul suma
    return print(suma) #returneaza valoarea sumei in consola

suma(5,6) #apeleaza functia suma
suma(-3,2.5)