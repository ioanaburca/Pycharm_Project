# # TEMA 2: Metoda input(), metode string, operatori, conditionale
#
# # A. RECOMANDAT (nivel USOR)
#
# # 1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva.
# # 2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare' (Daca nu ai facut-o deja)
# # 3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'.
# # Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si
# # sigur ti se vor intipari in minte mai bine.
# # Link catre video: https://www.itfactory.ro/8174437-intro-in-programare
#
# # B. OBLIGATORIU (nivel USOR -> MEDIU)
#
# # 1. Citeste de la tastatura numele, citeste apoi de la tastatura prenumele. Afiseaza cate caractere are numele complet
# # (nume + prenume), afisand propozitia 'Numele complet are x caractere.', unde x este numarul total de caractere.
#
# # Citesc de la tastatura numele si il salvez intr-o variabila
# # nume = input("Nume: ")
#
# # Salvez nr de caractere al numelui intr-o variabila, folosind functia len()
# # nr_nume = len(nume)
#
# # Citesc de la tastatura prenumele si il salvez intr-o variabila
# # prenume = input("Prenume: ")
#
# # Salvez nr de caractere al prenumelui intr-o variabila, folosind functia len()
# # nr_prenume = len(prenume)
#
# # Salvez nr total de caractere intr-o variabila
# # nr_total = nr_nume + nr_prenume
#
# # Afisez nr total de caractere, afisand propozitia indicata in enunt
# # print(f"Numele complet are {nr_total} caractere.")
#
# # 2. Citeste de la tastatura lungimea, citeste apoi de la tastatura latimea. Afiseaza aria dreptunghiului cu lungimea si
# # latimea citite de la tastatura, afisand propozitia 'Aria dreptunghiului este x.', unde x este valoarea ariei.
#
# # Citesc de la tastatura lungime si latime, si salvez rezultatele in variabile.
# # Trebuie sa ma asigur ca utilizatorul introduce date float.
# # lungime = float(input("Lungime: "))
# # latime = float(input("Latime: "))
#
# # Calculez aria dreptunghiului
# # arie = lungime * latime
#
# # Afisez aria dreptunghiului in propozitia indicata in enunt
# # print(f"Aria dreptunghiului este {arie}.")
#
# # 3. Avand stringul: 'Coral is either the stupidest animal or the smartest rock.', afisati de cate ori apare cuvantul
# # 'the' in acesta.
#
# prop = "Coral is either the stupidest animal or the smartest rock."
#
# # Pentru a ma asigura ca afisez de cate ori apare 'the' ca si cuvant de sine statator, pun si un spatiu la inceput
# # si la final.
# # print(prop.count(' the '))
#
# # 4. Folosing acelasi string de la punctul 2, inlocuieste cuvantul 'the' cu 'THE' peste tot in propozitie si printeaza
# # rezultatul.
#
# # print(prop.replace(' the ', ' THE '))
#
# # 5. Folosind acelasi string de la punctul 2, folositi un assert ca sa verificati daca acest string contine doar
# # numere.
#
# # assert prop.isnumeric()
#
# # 6. Exploreaza urmatoarele metode ajutatoare ale string-ului si scrie cel putin un exemplu de folosire pentru fiecare:
# # a. endswith()
#
# fruct_preferat = 'capsuni'
# assert fruct_preferat.endswith('i')
#
# # b. index()
#
# strada = 'Decebal'
# print(strada.index('e'))
#
# # c. lower()
#
# localitate = 'Cluj-Napoca'
# print(localitate.lower())
#
# # d. replace()
#
# combinatie_culori = 'rosu-galben'
# print(combinatie_culori.replace('galben', 'verde'))
#
# # e. strip()
#
# detalii_eveniment = '     Data evenimentului este in 2 martie.    '
# print(detalii_eveniment.strip())
#
# # f. split()
#
# culori_preferate = 'rosu,albastru,galben'
# print(culori_preferate.split(','))
#
# # ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# # Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.
#
# # Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# # sau citita de la tastatura, dupa preferinte si va fi o variabila int.
#
# x = int(input('Valoare x: '))
#
# # 6. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else.
#
# """
# daca conditie = True
#     se executa acest bloc de cod
# altfel
#     se executa acest bloc de cod
# """
#
# # 7. Verifica si afiseaza daca x este numar natural sau nu.
# # (un numar se considera natural daca este numar intreg mai mare ca 0)
#
# if x >= 0:
#     print(f"{x} este numar natural.")
# else:
#     print(f"{x} NU este numar natural.")
#
# # 8. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru (adica 0).
# if x > 0:
#     print(f"{x} este numar pozitiv.")
# elif x < 0:
#     print(f"{x} este numar negativ.")
# else:
#     print(f"{x} este neutru.")
#
# # 9. Verifica si afiseaza daca x este intre -2 si 13 (incluzand capetele de interval).
#
# if -2 <= x <= 13:
#     print(f"{x} este cuprins intre -2 si 13.")
# else:
#     print(f"{x} NU este cuprins intre -2 si 13.")
#
# # 10.
# # a. Declara o noua variabila numita y, de tip int.
#
# y = int(input("Valoare y: "))
#
# # b. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5.
#
# if x - y < 5:
#     print(f'Diferenta intre {x} si {y} este mai mica decat 5.')
# else:
#     print(f'Diferenta intre {x} si {y} este fie egala cu 5 sau mai mare.')
#
# # 11. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
#
# if not (5 <= x <= 27):
#     print('Numarul nu este intre 5 si 27.')
#
# # 12.
# # a. Declara o noua variabila numita y, de tip int.
#
# y = int(input("Valoare y: "))
#
# # b. Verifica si afiseaza daca x si y sunt egale. Daca nu, afiseaza care din ele este mai mare.
#
# if x == y:
#     print("Numerele x si y sunt egale.")
# elif x > y:
#     print(f"{x} este valoarea lui x si este mai mare decat y.")
# else:
#     print(f"{y} este valoarea lui y si este mai mare decat x.")
#
# # 13. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul
# # este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
#
# y = int(input("Valoare y: "))
# z = int(input("Valoare z: "))
#
# if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
#     print('Triunghiul este isoscel.')
# elif x == y == z:
#     print('Triunghiul este echilateral.')
# else:
#     print('Triunghiul este oarecare.')
#
# # 14. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# # Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
# litera = input("Introduceti o litera: ")
#
# # VARIANTA 1:
# if litera.isdigit():
#     print('Nu ai introdus o litera, ci altceva.')
# elif litera.upper() == 'A' or litera.upper() == 'E' or litera.upper() == 'I' or litera.upper() == 'O' or litera.upper() == 'U':
#     print('Litera este vocala.')
# else:
#     print('Litera nu este vocala.')
#
# # VARIANTA 2:
# vocale = 'aeiou'
#
# if litera.isdigit():
#     print('Nu ai introduc o litera, ci altceva.')
# elif litera in vocale or litera in vocale.upper():
#     print('Litera este vocala.')
# else:
#     print('Litera nu este vocala.')
#
# # 15. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# # Peste 9 => A
# # Peste 8 => B
# # Peste 7 => C
# # Peste 6 => D
# # Peste 4 => E
# # 4 sau sub => F
#
# nota = float(input("Care este nota primita? "))
# if 9 < nota <= 10:
#     nota = "A"
#     print(f"Nota primita in sistemul american este {nota}")
# elif nota >= 8:
#     nota = "B"
#     print(f"Nota primita in sistemul american este {nota}")
# elif nota >= 7:
#     nota = "C"
#     print(f"Nota primita in sistemul american este {nota}")
# elif nota >= 6:
#     nota = "D"
#     print(f"Nota primita in sistemul american este {nota}")
# elif nota > 4:
#     nota = "E"
#     print(f"Nota primita in sistemul american este {nota}")
# elif 4 >= nota >= 0:
#     nota = "F"
#     print(f"Nota primita este {nota}")
# else:
#     print('Nu a-ti introdus o nota de la 0 la 10.')
#
# # C. OPTIONAL (nivel > MEDIU) (s-ar putea sa ai nevoie de Google)
#
# # ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# # Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.
#
# # Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# # sau citita de la tastatura, dupa preferinte si va fi o variabila int.
#
# # 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre).
#
# # X este un numar intreg, dar acesta poate fi si negativ.
# # Astfel trebuie sa verificam daca valoarea absoluta a numarului este mai mare de 999.
# # Pentru asta folosim abs().
#
# if abs(x) > 999:
#     print('X are minim 4 cifre.')
# else:
#     print('X nu are minim 4 cifre.')
#
# # 2. Verifica daca x are exact 6 cifre.
#
# # X este un numar intreg, dar acesta poate fi si negativ.
# # Astfel trebuie sa verificam daca valoarea absoluta a numarului are exact 6 cifre.
# # Pentru asta folosim abs().
# if 100000 <= abs(x) <= 1000000:
#     print('X are exact 6 cifre.')
# else:
#     print('X nu are exact 6 cifre.')
#
# # 3. Verifica daca x este numar par sau impar.
#
# if x % 2 == 0:
#     print("Numarul este par.")
# else:
#     print("Numarul este impar.")
#
# # 4. Avand trei variabile x, y, z (toate int) (le poti declara in cod sau citi de la tastatura),
# # afiseaza in consola care este cel mai mare dintre ele.
# y = int(input("Valoare y: "))
# z = int(input("Valoare z: "))
# if x >= y and x >= z:
#     print(f'{x} este cel mai mare numar.')
# elif y >= x and y >= z:
#     print(f'{y} este cel mai mare numar.')
# else:
#     print(f'{z} este cel mai mare numar.')
#
# # 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid
# # sau nu. (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau
# # daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi).
#
# # Facem verificarea tinand cont de suma unghiurilor in triungi
# if x + y + z == 180 and x > 0 and y > 0 and z > 0:
#     print("Triunghiul este valid.")
# else:
#     print("Triunghiul NU este valid.")
#
# # Facem verificarea tinand cont de conditia ca suma a oricaror 2 laturi e mai mare decat a treia latura.
# if x + y > z and x + z > y and y + z > x:
#     print("Triunghiul este valid.")
# else:
#     print("Triunghiul NU este valid.")
#
# # 6.
# # a. Avand stringul: 'Coral is either the stupidest animal or the smartest rock', citește de la tastatura
# # un număr x de tip int.
# my_str = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input("Valoare x: "))
#
# # b. Afișează stringul fără ultimele x caractere.
#
# print(my_str[:-x])
#
# # Exemplu: dacă ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'
# # 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din
# # primele 5 caractere + ultimele 5 caractere.
#
# print(my_str[:5] + my_str[-5:])
#
# # 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start
# # al cuvântului rock - adică poziția in string la care începe cuvântul rock.
# # (hint: este o funcție care te ajuta sa faci asta).
#
# index_rock = my_str.index('rock')
# print(index_rock)
#
# # Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant.
#
# print(my_str[:index_rock])
#
# # Output asteptat: 'Coral is either the stupidest animal or the smartest '
# # 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel.
# # Se va folosi un assert.
# str_input = input("Introduceti un string: ")
# assert str_input[0].lower() == str_input[-1].lower()
#
# # Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care primul
# # si ultimul caracter este la fel (hint, te poti folosi de o functie pentru a face string-ul case insensitive)
# # 10. Avand stringul '0123456789', afiseaza doar numerele pare si apoi doar numerele impare.
# # (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step).
#
# str_numbers = '0123456789'
#
# # printam numerele pare
# print(str_numbers[0::2])
#
# # printam numerele impare
# print(str_numbers[1::2])
#
#
# # D. EXERCITII BONUS
#
# # 1. Vrem sa cream o aplicatie pentru achizitionare de bilete de avion care sa primeasca drept inputuri
# # urmatoarele informatii:
# # a. Varsta
# varsta = int(input("Varsta: "))
# # b. Insotit de mama
# insotit_de_mama = input("Insotit de mama - y/n: ")
# # c. Insotit de tata
# insotit_de_tata = input("Insotit de tata - y/n: ")
# # d. Pasaport
# are_pasaport = input("Are pasaport - y/n: ")
# # e. Act permisiune mama
# perm_mama = input("Permisiune mama - y/n: ")
# # f. Act permisiune tata
# perm_tata = input("Permisiune tata - y/n: ")
# # Conditii de imbarcare:
# # 1. Daca pers are varsta peste 18 ani si are pasaport.
# # 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti.
# # 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la
# # celalat parinte.
# # Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate variantele care crezi
# # ca ar trebui testate.
# # Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica daca expected results
# # sunt egale cu actual results.
# # Exemple:
# # 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# # 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
#
# if are_pasaport.lower() == 'y':
#     if varsta >= 18:
#         print("Da, se poate imbarca!")
#     else:
#         if insotit_de_tata.lower() == 'y' and insotit_de_mama.lower() == 'y':
#             print("Da, se poate imbarca!")
#         elif insotit_de_tata.lower() == 'y' and perm_mama.lower() == 'y':
#             print("Da, se poate imbarca!")
#         elif insotit_de_mama.lower() == 'y' and perm_tata.lower() == 'y':
#             print("Da, se poate imbarca!")
#         else:
#             print("Nu se poate imbarca!")
# else:
#     print("Nu se poate imbarca!")
#
#
# # 2. Joc de noroc
# # - Cauta pe net si vezi cum se genereaza un numar random.
# # - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# # Numarul salvat va fi generat random cu metoda gasita in online.
# import random
#
# number = random.randint(0, 9)
# # - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator.
# user_number = int(input("Alege un numar: "))
# # - Verifica si afiseaza daca utilizatorul a ghicit numarul.
# # - Vor exista 3 optiuni care vor trebui tratate:
# # a. Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# # b. Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# # c. Ai ghicit. Felicitari! Ai ales x si zarul a fost y.
#
# if user_number < number:
#     print(f"Ai pierdut! Ai ales un numar mai mic. Ai ales {user_number} dar era {number}.")
# elif user_number > number:
#     print(f"Ai pierdut! Ai ales un numar mai mare. Ai ales {user_number} dar era {number}.")
# else:
#     print(f"Ai ghicit. Felicitari! Ai ales {user_number} si zarul a fost {number}.")
#
# # 3. Verifica daca varsta introdusa de utilizator este mai mare
# # decat 18 ani.
# varsta = int(input("Varsta: "))
# if varsta >= 18:
#     print("Esti major")
# else:
#     print("Esti minor.")
#
# # 4. Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
# pret = float(input("Pret"))
# if pret <= 100:
#     print("Pretul introdus este mai mic sau egal de 100.")
# else:
#     print("Pretul este mai mare de 100.")
#
# # 5.
# # a. Citeste un numar de la tastatura.
# number = int(input("Number: "))
# # b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# # in fiecare situatie.
# if number % 2 == 0:
#     print("Numar par")
# else:
#     print("Numar impar")
#
# # 6.
# # a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
# viteza_medie = float(input("Viteza medie: "))
# # b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
# # c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
# if viteza_medie <= 50:
#     print("Viteza normala.")
# else:
#     print("Viteza depasita")
# # 7. Citeste de la tastatura varsta utilizatorului si afiseaza categoria
# # de varsta in care se incadreaza.
# # Tine cont de aceste categorii de varsta:
# # intre 0-18 ani: minor
# # intre 18-65 ani: adult
# # peste 65 ani: senior
# # varsta = int(input("Varsta: "))
# if varsta < 18:
#     print("minor")
# elif 18 <= varsta < 65:
#     print("adult")
# else:
#     print("senior")

# 8. Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
# cosul de cumparaturi, in functie de totalul cosului de cumparaturi
# Reducerea se aplica in felul urmator:
# - Total este intre 100 si 200 lei -> reducere 10%
# - Total intre 200 - 300 lei -> reducere 15%
# - Total intre 300-400 -> reducere 20 %
# - Total mai mare de 400 -> reducere 30 %.
# a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
# b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
# dupa aplicarea reducerii.
total = float(input("Totalul cosului de cumparaturi: "))
if 100 <= total <= 200:
    pret_final = total - 0.1 * total
elif 200 < total <= 300:
    pret_final = total - 0.15 * total
elif 300 < total <= 400:
    pret_final = total - 0.2 * total
elif total > 400:
    pret_final = total - 0.3 * total
else:
    pret_final = total
print(f"Pret final dupa reducere: {pret_final}")
