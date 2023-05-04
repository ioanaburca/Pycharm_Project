# # INPUT
#
# nume = input('Cum te numesti? ') # default - string
# varsta = int(input('Cati ani ai? ')) # fortam varsta sa fie un int
# print(nume)
# print(type(nume))
# print(varsta)
# print(type(varsta))
#
# # 1. Citeste de la tastatura un nume de produs.
# # Salveaza rezultatul intr-o variabila.
# # Afiseaza un mesaj care sa contina variabila salvata.
# nume_produs = input('Acesta este numele: ')
# print(f'Aici avem {nume_produs}')
#
# # 2. Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
# # Salveaza rezultatul intr-o variabila.
# # Afiseaza un mesaj care sa contina variabila salvata.
# pret = float(input('Acesta este pretul: '))
# print(f'Untul are pretul de {pret}')
#
# # INDEX
#
# info = 'Afara sunt 2 grade'
# print(info[0]) # => 'A' (primul caracter din string se afla la indexul 0)
# print(info[1]) # => 'f'
# print(info[5]) # => ' ' (la indexul 5 avem un spatiu gol)
#
# # 1. Se da variabila prop1 = 'Andy este prescurtarea de la Andrei"
# prop1 = 'Andy este prescurtarea de la Andrei'
# # a. Afiseaza primul caracter.
# print(prop1[0])  #A
# # b. Afiseaza al 4-lea caracter.
# print(prop1[3])  #y
# # c. Afiseaza ultimul caracter.
# print(prop1[-1]) # i
#
# # LUNGIMEA UNUI STRING
#
# info = 'Afara sunt 2 grade'
#
# # afisam lungimea string-ului info
# print(len(info)) # => 18

# 2. Se da string-ul prop2 = 'Masina e rosie.'
# Afiseaza lungimea string-ului prop2.
# prop2 = 'Masina e rosie.'
# print(len(prop2))

# SLICING

info = 'Afara sunt 2 grade'

# Extragem string-ul care incepe cu index-ul 0 pana la index-ul 1, inclusiv
print(info[0:2]) # => 'Af'
print(info[:2]) # => 'Af'

# Extragem string-ul care incepe cu index-ul 0 pana la indexul 4, inclusiv
print(info[0:5]) # => 'Afara'

# Daca nu specificam end_pos, se va extrage string-ul
# pana la ultimul caracter, inclusiv
print(info[6:])  # => 'sunt 2 grade'

# Daca nu specificam start_pos, se va extrage string-ul
# incepand cu primul caracter.
print(info[:5])  # => 'Afara'

## Inversare string
print(info[::-1]) # => 'edarg 2 tnus arafA'

# 3. Se da string-ul prop3 = 'Concertul va avea loc maine."
# prop3 = 'Concertul va avea loc maine.'
# a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
# var1 = prop3[0:9]
# print(var1)
# b. Extrage primele 3 caractere din prop3.
# print(prop3[:2])
# c. Afiseaza prop3 cu caracterele inversate.
# print(prop3[::-1])

# METODE AJUTATOARE STRING

# str1 = 'banana'
# print(str1.upper())

# 4. Se da string-ul my_str = 'vacanta'.
my_str = 'vacanta'
# a. Foloseste metoda find() pentru a afla primul index la care se gaseste caracterul 'a'.
# print(my_str.find('a'))
# print(my_str.find('ac'))
# b. Foloseste metoda count() pentru a afla de cate ori apare caracterul 'a' in my_str.

#print(my_str.count('a'))

# c. Foloseste metoda capitalize() pentru a scrie cuvantul cu prima litera mare.

# print(my_str.capitalize())

# OPERATORI ARITMETICI
# x = 2
# y = 3

# adunarea
# print(x + y) # 5
# scaderea
# print(y - x) # 1
# inmultirea
# print(x * y) # 6
# impartirea
# print(y / x) # 1.5
# restul impartirii
# print(y % x) # 1
# ridicarea la putere
# print(x ** y) # 2 la puterea 3 -> 8
# floor division
# print(y // x) # 3 // 2; 1.5 => 1

# inmultirea pe string-uri
# my_str = 'a'

# vreau sa afisez mesajul 'aaa'
# print(my_str + my_str + my_str)
# print(my_str * 3)


# 1. Se dau doua variabile, a = 10, b = 2.
# Efectueaza toate operatiile pe cele 2 variabile,
# folosind operatorii aritmetici.

# a = 10
# b = 2
# print(a + b) # 12
# print(a - b) # 8
# print(a * b) # 20
# print(a / b) # 5.0
# print(a % b) # 0
# print(a ** b) # 100
# 2.
# a. Citeste un numar de la tastatura.
# numar = int(input('Alege un numar:'))
# b. Verifica, folosind assert, daca numarul citit este numar par.
# assert numar % 2 == 0
# d. Foloseste metoda upper() pentru a scrie cuvantul cu litere mari.
print(my_str.upper())

# OPERATORI DE ATRIBUIRE
# 1. Rezolva exercitiul de la sectiunea de OPERATORI ARITMETICI
# folosind OPERATORII DE ATRIBUIRE.
# a = 10
# b = 2
# print(a + b) # 12
# a += b
# print(a - b) # 8
# a -= b
# print(a * b) # 20
# a *= b
# print(a / b) # 5.0
# a /= b
# print(a)

# OPERATORI LOGICI
# 1. Pentru fiecare din exemplele de mai jos, scrie intr-un comentariu
# rezultatul asteptat, apoi decomenteaza codul de la fiecare exemplu, pe rand
# si ruleaza exemplele si verifica output-ul.

# Exemplul 1:
# a = True
# b = False
# print(not(a)) # False
# print(not(b)) # True

# Exemplul 2:
# a = True
# b = False
# x = not(a) # False
# y = not(b) # True
# print(a or b) # True or False -> True
# print(x or y) # False or True -> True
# print(a or x) # True or False -> True
# print(x or b) # False or False -> False

# Exemplul 3:
# a = False
# b = False
# x = not(a) # True
# y = not(b) # True
# print(a and b) # False and False -> False
# print(a and x) # False and True -> False
# print(y and b) # True and False -> False
# print(x and y) # True and True -> True

# OPERATORI DE COMPARARE
# 1.
# a. Se da variabila num = 12
num = 12
# b. Folosind assert, verifica daca num citit este pozitiv.
assert num >= 0
# c. Folosind assert, verifica daca num este mai mare decat 5.
assert num > 5
# d. Folosind assert, verifica daca num este mai mic decat 25.
assert num < 25
# e. Folosind assert, verifica daca num este intre 0 si 20
assert num > 0 and num < 20
assert 0 < num < 20

# IF
# x = 5
# if x == 5:
#     print("x este egal cu 5")
# print("final cod")

# nota_de_trecere = 4.5
# nota = float(input('alege nota'))
# if nota >= nota_de_trecere:
#     print(f'Ai luat nota {nota}')
#     print('Felicitari, ai trecut examenul!')
# constanta = are o valoare stabila, nu ne dorim sa o schimbe nimeni
# standardul este sa o scriem cu litere mari
NOTA_DE_TRECERE = 4.5
nota = float(input('Alege nota'))
if nota >= NOTA_DE_TRECERE:
    print(f'Ai luat nota {nota}')
    print('Felicitari ai trecut examenul')
else:
    print(f'Ai luat doar nota {nota}')
    print('Ne vedem la vara! Ai picat examenul')