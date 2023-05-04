# definim o variabila cu numele marca_masina
marca_masina = 'Volvo'

#  printam variabila marca_masina
# print(marca_masina)

# definim o variabila cu numele model_masina
model_masina = 'XC 60'

#  ASA NU
# marcaMasina

fructul_preferat = 'mar'
propozitie1 = 'valoare'
propozitie2 = 'prop2'

my_var = 5
my_Var = 10

nume = 'Maria'
# print(nume)
nume = 'Ana'
# print(nume)

x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

a = b = 'Apple'
# print(a)
# print(b)

# definim variabile de tip string
# prop1 = 'Ana este afara.'
# prop2 = "Maria este in casa."

# concatenare string-uri
nume = 'Burca'
print(nume)

prenume = 'Ioana'
# print(nume + '  ' + prenume)
# print('Numele meu este ' + ' ' + nume + ' ' + prenume)

# TIPURI DE DATE
# 1.
# a. Defineste o variabila de tip int, numita 'latime'.
latime = 10

# b. Defineste o variabila de tip string, numita 'descriere'.
descriere = 'inghetata'

# c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
pret = 2.5
discount = 0.5

# d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
initializat = False

# e. Printeaza variabilele definite la punctele anterioare.
print(latime)
print(descriere)
print(pret)
print(discount)
print(initializat)

# definim o variabila string
culoare = 'rosu'
# afisam in consola tipul variabilei culoare
print(type(culoare)) # <class 'str'>

pret1 = 12.3
print(type(pret1))

nume_produs = 'Canapea'
pret = 200
print('Produsul ' + nume_produs + ' costa ' + str(pret) + ' lei.')
print(f'Produsul {nume_produs} costa {pret} lei.')

# 6.
# a. Defineste doua variabile: nume (string) si varsta (int).
nume = 'Matei'
varsta = 25

# b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
print(f'Numele tau este {nume} si ai varsta {varsta}')

# TYPE si TYPE CASTING
# 7.
# a. Defineste o variabila de tip int, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
a = 12
print(a)
print(type(a))

# b. Defineste o variabila de tip float, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
a = 12.5
print(a)
print(type(a))

# c. Defineste o variabila de tip string, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
a = 'rosu'
print(a)
print(type(a))

# d. Defineste o variabila de tip bool, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
d = False
print(d)
print(type(d))

a = 1
# assert a == 1
# print('trec pe aici')
# assert a == 2
# print('Nu mai trec pe aici')

# ASSERT
# 10.
# a. Defineste o variabila string si da-i valoarea "10".
valoare = '10'

# b. Verifica daca string-ul definit la punctul a este egal cu "10".
assert valoare == '10'
print('Am trecut')

# c. Verifica daca string-ul definit la punctul a este egal cu 10.
assert valoare == '10'
print('Nu am trecut')