# # 1. Explica intr-un comentariu ce este o variabila de tip string.
# # variabila de tip string este o variabila in care se poate adauga un sir de caractere delimitate de ghilimele
#
# # 2. Defineste o variabila string, numita descriere si afiseaz-o.
# descriere = 'pisica'
# print(descriere)
#
# # 3. Defineste 3 variabile: oras, strada si nr.
# oras = 'Bacau'
# strada = 'Florilor'
# nr = 10
#
# # a. Afiseaza aceste variabile intr-o propozitie, folosind concatenarea string-urilor.
# print('Locuiesc in orasul ' + oras + ' pe strada ' + strada + ' la numarul ' + str(nr))
#
# # b. Afiseaza aceste variabile intr-o propozitie, folosind f-strings.
# print(f'Locuiesc in {oras} pe {strada}  la numarul  {nr}')
#
# # 4. Se da variabila string, nume_complet = 'Pop Maria Ioana'.
# nume_complet = 'Pop Maria Ioana'
#
# # a. Afiseaza primul element din string.
# print(nume_complet[0:3])
#
# # b. Afiseaza al doilea prenume.
# print(nume_complet[10:])
#
# # c. Afiseaza de cate ori apare litera 'a' in nume_complet.
# print(nume_complet.count('a'))
#
# # d. Inverseaza string-ul si afiseaza rezultatul.
# print(nume_complet[::-1])
#
# # e. Inlocuieste al doilea prenume cu 'Elena'.
# nume_complet1 = nume_complet.replace('Ioana', 'Elena')
# print(nume_complet1)
#
# # f. Afiseaza caracterele de la indexul 5 la indexul 9 (inclusiv).
# print(nume_complet[5:10])
#
# # g. Afiseaza caracterele de la inceputul string-ului pana la index-ul 8 (inclusiv).
# print(nume_complet[:9])
#
# # 5. Citeste de la tastatura culoarea preferata a utilizatorului si salveaza rezultatul intr-o variabila.
# culoare_preferata = input('Introdu culoarea preferata: ')
# culoare = culoare_preferata
# print(culoare)
#
# # a. Determina lungimea inputului citit de la tastatura.
# print(len(culoare))
#
# # b. Determina tipul inputului citit de la tastatura.
# print(type(culoare))
#
# # c. Transforma inputul de la utilizator in text cu litere mari si afiseaza-l.
# print(culoare.upper())
#
# # d. Transforma inputul de la utilizator in text care incepe cu litera mare si restul sunt litere mici.
# # Afiseaza rezultatul.
# print(culoare.capitalize())
#
# # 6. Se da variabila my_var = '1234'. Verifica daca my_var este compus doar din numere.
# my_var = '1234'
# print(my_var.isnumeric())
#
# # 7. Se da variabila anotimp = 'primavara'. Verifica daca anotimp se termina in 'vara'.
# anotimp = 'primavara'
# print(anotimp.endswith('vara'))
#
# # 8. Citeste de la tastatura numarul de zile ramase pana la vacanta.
# # Verifica, folosind assert, daca numarul de zile este mai mare de 7 zile.
# nr_zile = int(input('Introdu nr de zile pana la vacanta: '))
# assert nr_zile > 7
#
#
# # 9. Citeste de la tastatura pretul cosului de cumparaturi. Afiseaza pretul cu un discount de 25%.
# pret_cos = float(input('Introdu pretul cosului de cumparaturi: '))
# print(pret_cos - (pret_cos * 25 / 100))
#
# # 10. Se da string-ul: zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'.
# # Transforma string-ul in lista, folosindu-te de o metoda ajutatoare de pe string.
# zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'
# print(zile_sapt.split())
#
# # 11. Se citeste de la tastatura 2 string-uri. Verifica daca al doilea string se gaseste in primul.
# string1 = input('Introdu string1: ')
# string2 = input('Introdu string2: ')
# if string2 in string1:
#     print('Stringul se gaseste aici.')
# else:
#     print('Stringul nu se gaseste aici.')
#
# # 12. Scrie un program care solicita utilizatorului sa introduca varsta sa
# # și returneaza un mesaj personalizat, in funcție de varsta introdusa.
# # Daca varsta este mai mare sau egala cu 18, programul trebuie sa afiseze
# # mesajul "Esti major si poti vota".
# # In caz contrar, programul trebuie sa afiseze mesajul "Esti minor si nu poti vota inca".
# varsta = int(input('Introdu varsta ta: '))
# if varsta >= 18:
#     print('Esti major si poti vota.')
# else:
#     print('Esti minor si nu poti vota inca')
#
# # 13. Scrie un program care primeste un pret de la tastatura si afiseaza
# # un mesaj daca prețul este mai mare sau mai mic decât 100 de lei.
# pret = float(input('Introdu pretul: '))
# if pret > 100:
#     print('Pretul este mai mare.')
# else:
#     print('Pretul este mai mic.')
#
# # 14. Citeste doua numere intregi de la tastatura. Printeaza produsul dintre cele doua numere
# # daca acesta este mai mic sau egal decat 1000, altfel printeaza suma lor.
# numar_intreg1 = int(input('Introdu nr: '))
# numar_intreg2 = int(input('Introdu nr: '))
# if (numar_intreg1 * numar_intreg2) <= 1000:
#     print(numar_intreg1 * numar_intreg2)
# else:
#     print(numar_intreg1 + numar_intreg2)
#
# # 15. Se dau doua liste:
# lista_1 = [10, 20, 30, 40, 50, 10]
# lista_2 = [1, 2, 3, 4, 5]
#
# # Pentru fiecare lista verifica daca primul si ultimul element sunt egale.
# # In functie de rezultat, afiseaza un mesaj.
# if lista_1[0] == lista_1[5]:
#     print('Lista 1 are primul element = cu ultimul element')
# else:
#     print('Lista 1 nu are primul element = cu ultimul element')
#
# if lista_2[0] == lista_2[4]:
#     print('Lista 2  are primul element = cu ultimul element')
# else:
#     print('Lista 2 nu are primul element = cu ultimul element')
#
#
#
# # 16. Scrie un program care afiseaza de cate ori apare litera 'e' in
# # stringul
# str_1 = 'Emma is a sofware developer.'
# print(str_1.count('e'))
#
#
# # 17. Scrie un program in care citesti de la tastatura doua nr intregi,
# # numite base si exponent.
# # Afiseaza intr-un mesaj sugestiv, valoarea lui base la puterea exponent.
# # Atentie: indiferent daca utilizatorul a introdus un numar pozitiv sau negativ
# # ca si exponent, trebuie sa ridici base la puterea exponent pozitiv.
# # hint: exploreaza functia abs() si vezi cum o poti folosi
# base = int(input('Introdu valoarea lui base:'))
# exponent = int(input('Introdu valoarea lui exponent:'))
# print(f'Valoarea lui base la puterea exponent este', (base ** abs(exponent)))

# 18. Scrie un program in care se citeste de la tastatura un string.
# Daca string-ul are numar impar de caractere, afiseaza un string care
# contine primul caracter, caracterul din mijloc al string-ului
# citit de la tastatura si ultimul caracter.
# Daca string-ul are numar par de caractere, afiseaza un string care contine doar primul
# si ultimul caracter  al string-ului citit de la tastatura.
# strazi = input('Introdu numele:')
# if not len(strazi) % 2 == 0:
#     print([strazi[0], strazi[round(len(strazi) / 2)], strazi[len(strazi) - 1]])
# else:
#     print([strazi[0], strazi[len(strazi) - 1]])


# 19. Se dau doua variabile:
str1 = 'Abc'
str2 = 'Xyz'
# Creeaza o variabila string, str3 formata din:
# - primul caracter din str1 cu litera mica
# - primul caracter din str2 cu litera mare
# - al doilea caracter din str1 cu litera mare
# - al doilea caracter din str2 cu litera mare
# - al treilea caracter din str1 cu litera mare
# - al treilea caracter din str2 cu litera mica

str3 = str1[0].lower(), str2[0].capitalize(), str1[1].upper(), str2[1].upper(), str1[2].upper(), str2[2].lower()
print(str3)

# 20. Se da string-ul my_str = 'Emma is a data scientist who knows Python. Emma works at google.'
# Afiseaza ultima pozitie a substring-ului "Emma" in string-ul dat.
# HINT: vezi metoda ajutatoare string rstrip()
my_str = 'Emma is a data scientist who knows Python. Emma works at google.'
my_str2 = my_str.split()
my_str3 = my_str2[0]
print(my_str3[-1])