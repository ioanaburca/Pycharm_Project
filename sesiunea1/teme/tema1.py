# TEMA_1

# A. RECOMANDAT (nivel USOR)

# 1. Revizualizeaza inregistrarea sesiunii 1 si ia notite
# 2. Vizualizeaza cursul "PRIMII PASI IN PROGRAMARE" (daca nu ai facut-o deja), sectiunea "Variable si Tipuri de date"
# 3. Vizualizeaza cursul "PRIMII PASI IN PROGRAMARE", sectiunea "Operatori si Flow Control".
# LINK curs "PRIMII PASI IN PROGRAMARE": https://www.itfactory.ro/8174437-intro-in-programare/


# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila.
# variabila este o zona dintr-o memorie a calculatorului, o cutiuta unde punem valori

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool.
# string
nume_strada = 'Lalelelor'
# int
nr_strada = 10
# float
km = 5.2
# bool
strada_noua = True
# Valorile le alegeti voi dupa preferinte.

# 3. Utilizati functia type(), pentru a verifica daca variabilele declarate la punctul 2 au tipul de date asteptat.
print(type(nume_strada))  #str
print(type(nr_strada))    #int
print(type(km))           #float/double
print(type(strada_noua))  #bool

# 4. Rotunjiti variabila definita ca tip float, folosindu-va de functia round() si salvati aceasta modificare in aceeasi
# variabila (suprascriere). Verificati apoi tipul acesteia.
km = round(km)
print(km)
print(type(km))

# 5. Folositi functia print() pentru a printa in consola 4 propozitii, folosind cele 4 variabile.
# (Rezolvati nepotrivirile de tip prin ce modalitate doriti)
print(f'Eu locuiesc pe strada {nume_strada}')
print(f'Stau pe strada cu nr. {nr_strada}')
print(f'Distanta de la casa la munca este de {km} km')
print(f'Nu este {strada_noua}  ca este strada noua')

# 6.
# a. Defineste o variabila float cu valoarea 1.5 .
kg = 1.5

# b. Verifica daca variabila este egala cu 1.5 .
assert kg == 1.5
print('Este usor')

# c. Verifica daca variabila este egala cu true. Ce observi?
# assert kg == True
# print('Nu este usor')
# codul nu a trecut deoarece assert-ul este false nu este acelasi tip de date

# d. Cum poti face ca assert-ul de la punctul c sa treaca?
assert bool(kg) == True
print('Nu este usor')

# C. OPTIONAL (nivel > MEDIU)

# 1. Citeste de la tastatura un string de dimensiune impara. Afiseaza caracterul din mijloc.
prop = input(" Ex 1: Introduceti un sir de caractere de dimensiune impara:\n")
mid_char = len(prop) # 2
print(f"Caracterul din mijloc este {prop[mid_char]}")

# 2. Folosind assert, verificati daca un string este palindrom.
# citim un string de la tastatura si salvam rezultatul in variabila prop
prop = input("Ex 2: Introduceti un sir de caractere: \n")

# PALINDROM = string care citit de la stanga la dreapta sau de la dreapta la stanga ramane neschimbat.

# verificam daca prop este egal cu prop inversat
# daca prop nu e palindrom, vom avea eroare si se va afisa mesajul "Cuvantul introdus nu e palindrom"
assert prop == prop[::-1], "Cuvantul introdus nu e palindrom."

# daca prop este palindrom, atunci acest mesaj se va afisa.
print("Cuvantul introdus e palindrom.")

# 3. Folosind o singura linie de cod, citeste un string de la tastatura (ex: 'alabala portocala') si salveaza fiecare
# cuvant intr-o variabila. Printeaza variabilele generate pentru verificare.

a, b = input('Ex 3: Introduceti un string: \n').split(' ')
print(a, b)

# 4. Citeste un string de la tastatura (ex: 'alabala portocala'). Salveaza primul caracter din string intr-o variabila.
# Capitalizeaza acest caracter peste tot in string, mai putin primul si ultimul caracter.
# Exemplu 1:
#   input: 'alabala portocala'
#   output: 'alAbAlA portocAla'
# Exemplu 2:
#   input: 'maria are mere'
#   output: 'maria are Mere'
# Exemplu 3:
#   input: 'aritmetica'
#   output: 'aritmetica'

my_str = input('Ex 4: Introduceti un string: \n')
my_char = my_str[0]

# cream un nou string, folosind slicing, care sa contina toate caracterele, mai putin primul caracter
my_str2 = my_str[1:]

# folosim metoda ajutatoare replace(), pentru a inlocui toate caracterele egale cu variabila 'my_char',
# cu varianta capitalizata.
# pentru a capilatiza un string/caracter, folosim metoda upper()
my_str3 = my_str2.replace(my_char, my_char.upper())

# se poate ca si ultimul caracter sa fie acelasi ca primul caracter din string-ul primit ca output.
# atunci vom transforma ultimul caracter din 'my_str3', sa ne asiguram ca e mereu cu litera mica.
# afisam rezultatul final folosind f string
print(f"{my_char}{my_str3[:-1]}{my_str3[-1].lower()}")

# 5. Citeste un user de la tastatura. Citeste apoi o parola de la tastatura. Afiseaza: 'Parola pentru userul x este ***
# si are y caractere.', unde x este user-ul citit de la tastatura, iar y lungimea parolei introduse la tastatura.
# Numarul de * din stringul afisat se va calcula dinamic, avand atatea * cate caractere exista in parola.
# Exemplu:
#   - daca parola introdusa este 'abcd', vom avea ***
#   - daca parola introdusa este 'abcdef', vom avea ******.

user = input("User:")
parola = input("Parola: ")
parola_ascunsa = '*' * len(parola)
print(f"Parola pentru userul {user} este {parola_ascunsa} si are {len(parola)} caractere. ")