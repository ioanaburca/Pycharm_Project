# TEMA 2: Metoda input(), metode string, operatori, conditionale

# A. RECOMANDAT (nivel USOR)

# 1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva.
# 2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare' (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'.
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si
# sigur ti se vor intipari in minte mai bine.
# Link catre video: https://www.itfactory.ro/8174437-intro-in-programare

# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. Citeste de la tastatura numele, citeste apoi de la tastatura prenumele. Afiseaza cate caractere are numele complet
# (nume + prenume), afisand propozitia 'Numele complet are x caractere.', unde x este numarul total de caractere.


# print(len('Burca' + 'Ioana'))
# print(f'Numele complet are ' + str(len('Burca' + 'Ioana')) + ' caractere')

# 2. Citeste de la tastatura lungimea, citeste apoi de la tastatura latimea. Afiseaza aria dreptunghiului cu lungimea si
# latimea citite de la tastatura, afisand propozitia 'Aria dreptunghiului este x.', unde x este valoarea ariei.


# print(4 * 2)
# print(f'Aria dreptunghiului este ' + str(4 * 2))


# 3. Avand stringul: 'Coral is either the stupidest animal or the smartest rock.', afisati de cate ori apare cuvantul
# 'the' in acesta.

prop = 'Coral is either the stupidest animal or the smartest rock.'
# print(prop.count(' the '))
# il punem pe 'the' cu spatiu pentru ca sunt 2 cuvinte de sine stattoare

# 4. Folosing acelasi string de la punctul 2, inlocuieste cuvantul 'the' cu 'THE' peste tot in propozitie si printeaza
# rezultatul.

# print(prop.replace(' the ', ' THE '))


# 5. Folosind acelasi string de la punctul 2, folositi un assert ca sa verificati daca acest string contine doar
# numere.

# assert prop == int
# print(True)

# 6. Exploreaza urmatoarele metode ajutatoare ale string-ului si scrie cel putin un exemplu de folosire pentru fiecare:

# a. endswith() = il transforma cumva in bool si ii da valoarea True
# floare = 'lalea'
# print(floare.endswith('a'))

# b. index() = imi returneaza indezul primei litere
# strada = 'Stau pe strada rozelor'
# print(strada.index('S')) # 0

# c. lower() = imi returneaza totul cu litere mici
#marca_tv = 'Samsung'
#print(marca_tv.lower()) #samsung

# d. replace() = adica inlocuieste ceva
# prop3 = 'Primavara este frumoasa'
# prop3 = prop3.replace('frumoasa', 'ploioasa')
# print(prop3)

# e. strip() = elimina caractere din string
# prop4 = 'Cerul e albastru!'
# print(prop4.strip('!'))


# f. split() = imparte string-ul printr-un separator

# text = 'Buna, sunt Ioana!'
# print(text.split(','))


# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.

# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.

# 6. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else.
# daca o variabila indeplineste conditia din if intra in acesta, daca nu, blocul de cod se foloseste de else

# 7. Verifica si afiseaza daca x este numar natural sau nu.
# (un numar se considera natural daca este numar intreg mai mare ca 0)

# numar = 1
# if numar > 0:
#     print('numarul este mai mare ca 0')
# else:
#     print('numarul nu este mai mare ca 0')


# 8. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru (adica 0).

# nr = 3
# if nr > 0:
#     print('pozitiv')
# elif nr == 0:
#     print('neutru')
# else:
#     print('negativ')


# 9. Verifica si afiseaza daca x este intre -2 si 13 (incluzand capetele de interval).

# x = 4
# if x >= -2 and x <= 13:
#     print(True)
# else:
#     print(False)

# 10.
# a. Declara o noua variabila numita y, de tip int.

# y = 2

# b. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

# print(x - y)
# diferenta = x - y
# if diferenta < 5:
#     print(True)
# else:
#     print(False)

# 11. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

# x = 28
# if x not in range(5, 27):
#     print(True)

# 12.
# a. Declara o noua variabila numita y, de tip int.

# y = 6

# b. Verifica si afiseaza daca x si y sunt egale. Daca nu, afiseaza care din ele este mai mare.

# if x == y:
#     print('Sunt egale')
# elif (x > y):
#     print('x > y')
# else:
#     print('y > x')



# 13. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul
# este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).

# x = 6
# y = 6
# z = 4
# if x == y == z:
#     print('Echilateral')
# elif (x == y) or (x == z) or (y == z):
#     print('Isoscel')
# else:
#     print('Nicio latura nu e egala')

# 14. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

# litera = input('Introdu caracter')
# if litera.lower() in ('a', 'e', 'i', 'o', 'u' ):
#     print('Vocala')
# elif litera.upper() in ('A', 'E', 'I', 'O', 'U'):
#     print('Vocala')
# else:
#     print('Consoana')

# 15. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:

# nota = int(input('introdu nota'))
# if nota > 9:
#     print('A')
# elif nota > 8:
#     print('B')
# elif nota > 7:
#     print('C')
# elif nota > 6:
#     print('D')
# elif nota > 4:
#     print('E')
# elif nota < 4:
#     print('F')



# C. OPTIONAL (nivel > MEDIU) (s-ar putea sa ai nevoie de Google)

# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.

# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.

# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre).
# aici am gasit doua varinate
# x = 1234
# x = len(str(x))
# if x >= 4:
#     print('X are minim 4 caractere')
# else:
#     print('X nu are minim 4 caractere')

# x = -789
# count = 0
# while(x > 0):
#     count = count + 1
#     x = x // 10
# if count >= 4:
#     print('x este format din minim 4 cifre')
# else:
#     print('x nu este format din minim 4 cifre')

# 2. Verifica daca x are exact 6 cifre.

# x = int(input('Introdu X: '))
# if x < 0 and len(str(x)) > 4:
#     print('X are minim 4 cifre')
# if x > 0 and len(str(x)) >= 4:
#     print('X are minim 4 cifre')
# else:
#     print('X are sub 4 cifre')

# if x > 0 and len(str(x)) == 6:
#     print('X are exact 6 cifre')
# if x < 0 and len(str(x)) == 7:
#     print('X are exact 6 cifre')
# else:
#     print('X nu are 6 cifre')

# if x == 6:
#     print('Are 6 caractere')
# else:
#     print('Nu are 6 caractere')

# 3. Verifica daca x este numar par sau impar.
# am impartit x (1234) la 2, restul fiind 0

# if (x % 2) == 0:
# print('X este nr par')
# else:
# print('Nr. este impar')


# 4. Avand trei variabile x, y, z (toate int) (le poti declara in cod sau citi de la tastatura),
# afiseaza in consola care este cel mai mare dintre ele.

# x = 1
# y = 2
# z = 3
# print(max([1,2,3]))  # raspuns asteptat 3

# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid
# sau nu. (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau
# daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi).

# x = 4
# y = 4
# z = 2
# if (z + y + z) == 180:
#     print('Triunghiul este valid')
# else:
#     print('Triunghiul nu este valid')

# x = 30
# y = 30
# z = 60
# sum = (x + y + z)
# if sum == 180 and (x>0) and (y>0) and (z>0):
#     print('Triunghiul este valid')
# else:
#     print('Triunghiul nu este valid')

# a = 30
# b = 30
# c = 60
# if x > 0 and y > 0 and z > 0 and a > 0 and b > 0 and c > 0:
#     if suma_unghiuri == 180 or a + b > c:
#         print('Este un triunghi valid')
#     elif suma_unghiuri == 180 or a + c  > b:
#         print('Este un triunghi valid')
#     elif suma_unghiuri == 180 or b + c  > a:
#         print('Este un triunghi valid')
#     else:
#         print('Nu este un triunghi valid')
# else:
#     print('Nu avem deloc triunghi')


# 6.
# a. Avand stringul: 'Coral is either the stupidest animal or the smartest rock', citește de la tastatura
# un număr x de tip int.


# string = 'Coral is either the stupidest animal or the smartest rock';
# x = int(input('Tasteaza numarul dorit:'))

# b. Afișează stringul fără ultimele x caractere.
# Exemplu: dacă ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'

# if x > 0:
# print(string[:-x])
# else:
# print(string[:x])

# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din
# primele 5 caractere + ultimele 5 caractere.

# prop_1 = 'Coral is either the stupidest animal or the smartest rock';
# prop_1 = print(prop_1[0:5] + prop_1[-5:]) # string = 'Coral rock'

# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start
# al cuvântului rock - adică poziția in string la care începe cuvântul rock.
# (hint: este o funcție care te ajuta sa faci asta).

# string = 'Coral is either the stupidest animal or the smartest rock';
# rock_index = string.index('rock');
# print(rock_index)

# Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant.

# print(string[0:rock_index])
# Output asteptat: 'Coral is either the stupidest animal or the smartest '

# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel.
# Se va folosi un assert.
# Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care primul
# si ultimul caracter este la fel (hint, te poti folosi de o functie pentru a face string-ul case insensitive)

# prop = input('Introdu un string : ')
# prop = prop.lower()
# assert prop[0] == prop[-1]
# print('Caracterele sunt la fel')


# 10. Avand stringul '0123456789', afiseaza doar numerele pare si apoi doar numerele impare.
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

# string = '0123456789'
# print(f'Numerele pare {string[0:len(string):2]'})
# print(f'Numerele pare {string[1:len(string):2]}')


# D. EXERCITII BONUS

# 1. Vrem sa cream o aplicatie pentru achizitionare de bilete de avion care sa primeasca drept inputuri
# urmatoarele informatii:
# a. Varsta
# b. Insotit de mama
# c. Insotit de tata
# d. Pasaport
# e. Act permisiune mama
# f. Act permisiune tata
# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport.
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti.
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la
# celalat parinte.
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate variantele care crezi
# ca ar trebui testate.
# Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica daca expected results
# sunt egale cu actual results.
# Exemple:
# 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca

#  1 este adevărat, iar 0 sau orice altceva e Fals
# varsta = int(input('Introdu varsta: '))
# cu_mama = int(input('Este insotit de mama: '))
# cu_tata = int(input('Este insotit de tata: '))
# pasaport = int(input('Are pasaport: '))
# act_mama = int(input('Are act de la mama: '))
# act_tata = int(input('Are act de la tata: '))
# if varsta >= 18 and pasaport == 1:
#     print('Ma pot imbarca')
# elif (varsta < 18 and pasaport == 1 and cu_mama == 1 and cu_tata == 1):
#     print('Ma pot imbarca')
# elif varsta < 18 and pasaport == 1 and cu_mama == 1 and act_tata == 1:
#     print('Ma pot imbarca')
# elif varsta < 18 and pasaport == 1 and cu_tata == 1 and act_mama == 1:
#     print('Ma pot imbarca')
# else:
#     print('Nu ma pot imbarca')

# 2. Joc de noroc
# - Cauta pe net si vezi cum se genereaza un numar random.
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online.
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator.
# - Verifica si afiseaza daca utilizatorul a ghicit numarul.
# - Vor exista 3 optiuni care vor trebui tratate:
# a. Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# b. Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# c. Ai ghicit. Felicitari! Ai ales x si zarul a fost y.

# import random
# dice_roll = random.randint(0,9)
# print(dice_roll)
# numar_ales = int(input('Alege numar: '))
# if numar_ales < dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ales} dar a fost {dice_roll}.')
# elif numar_ales > dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ales} dar a fost {dice_roll}.')
# else:
#     print(f'Ai ghicit. Felicitari! Ai ales {numar_ales} si zarul a fost {dice_roll}.')

# 3. Verifica daca varsta introdusa de utilizator este mai mare
# decat 18 ani.

# varsta = int(input('Tasteaza varsta ta:'))
# if varsta > 18:
#     print('este mai mare')
# else:
#     print('nu este mai mare')

# 4. Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.

# pretul = int(input('Introdu pretul:'))
# if pretul <= 100:
#     print('pret mai mic sau egal cu 100 dolari')
# else:
#     print('pret mai mare de 100 dolari')


# 5.
# a. Citeste un numar de la tastatura.
# b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.

# nr = int(input('Tasteaza un numar:'))
# if nr % 2 == 0:
#     print('numarul e par')
# elif nr % 2 != 0:
#     print('numarul e impar')

# 6.
# a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
# b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
# c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".

# viteza = int(input('Introdu viteza conducatorului:'))
# if viteza == 50 or viteza < 50:
#     print('Viteza normala')
# else:
#     print('Viteza depasita')

# 7. Citeste de la tastatura varsta utilizatorului si afiseaza categoria
# de varsta in care se incadreaza.
# Tine cont de aceste categorii de varsta:
# intre 0-18 ani: minor
# intre 18-65 ani: adult
# peste 65 ani: senior

# varsta = int(input('Introdu varsta ta: '))
# if varsta >=0 and varsta < 18 :
#     print('Esti minor')
# elif varsta >= 18 and varsta <= 65:
#     print('Esti adult')
# elif varsta > 65:
#     print('Senior')
# else:
#     print('Nu te incadrezi in nici o categorie')

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

total =  int(input('Totalul cosului de cumparaturi este:'))
if total >= 100 and total <= 200:
    print(total - (total * 10 / 100))
elif total >= 200 and total <= 300:
    print(total - (total * 15 / 100))
elif total >= 300 and total <= 400:
    print(total -(total * 20 /100 ))
elif total >= 400:
    print(total - (total * 30 / 100))
else:
    print('nu are reducere')