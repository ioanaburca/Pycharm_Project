"""
1.Git setup

OBLIGATORIU!
Creati-va cont de github si incarcati intr-un repo nou tot ce am facut pana acum la ore
Curs git/github
https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3
"""
"""
un repo este un loc in git/ cloud unde punem un proiect scris ca sa il vada angajatorul
acest git are un trunchi comun unde se tot incarca/actualizaza cos
git este un tool de versionare care ne ajuta sa comunicam cu github sa ajunga codul nostru in cloud
workflows - cand facem un remote clone se cloneaza si se face o copie
ca o comparatie ca sa inteleg ce face fiecare
git add = adaugam fisierele in plic si se fac din rosii verzi
git commit = scriem  ceva pe plicul sigilat
git push = plicul deja pleaca spre desinatar
git pull = s-ar putea in remote repo sa avem un cod actualizat
si trebuie sa fiu la zi si trebuie sa iau informatia actualizata din plic
daca lucrez doar eu cel mai probabil nu il voi folosi, dar daca e prooect si colegi, da
git checkout
"""

"""
!! 2. Faceti urmatoarele exercitii dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
"""

"""
1. ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
"""
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(cls):
        print("Cel mai probabil am colturi")


"""
2. INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
"""

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f"Getter: Latura este {self.__latura}")
        return self.__latura

    @latura.setter
    def latura(self, value):
        print(f"Setter: Noua latura este {value}")
        self.__latura = value

    @latura.deleter
    def latura(self):
        print(f"Deleter: Am sters latura")
        self.__latura = None

"""
3. Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)
"""

"""
4. POLYMORPHISM 
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’


Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
"""
class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f"Raza cercurlui este: {self.__raza}")

    @raza.setter
    def raza(self, value):
        print(f"Noua valoare a razei este: {value}")
        self.__raza = value

    @raza.deleter
    def raza(self):
        print("Am sters valoarea razei.")
        self.__raza = 0

    def aria(self):
        aria_cercului = self.PI * self.__raza * self.__raza

    def descrie(self):
        print("Eu nu am colturi")
"""
5. Actualizati proiectul pe github facand un push la noul cod
In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public

Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4
"""