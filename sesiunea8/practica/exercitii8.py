"""
Recapitulare OOP ( Clase, obiecte, cei 4 piloni OOP)
"""

"""
1. Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""

from abc import ABC, abstractmethod
class AbstractVideo(ABC):
    @abstractmethod
    def show_details(self):
        pass

    def play(self):
        print('Video is playing')
"""
2. Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""

class Videoclip(AbstractVideo):

    def init(self, title, duration):
        self.title=title
        self.duration=duration

    def show_details(self):
        print(f'{self.title} has a duration {self.duration} minutes')

v = Videoclip('Titlu', 75)

print(v.title)
print(v.duration)

v.play()
v.show_details()

"""
3. 
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""

class Movie(Videoclip):

    def init(self, title, duration, genre, director, actors):
        super().init(title, duration)
        self.genre = genre
        self.director = director
        self.actors = actors

    @property
    def director(self):
        return self.director

    @director.getter
    def director(self):
        print("Get")
        return self.director

    @director.setter
    def director(self, value):
        print("Set")
        self.director = value

    @director.deleter
    def director(self):
        print("Delete")
        self.director = None

    def show_details(self):
        super().show_details()
        print(f"Is directed by {self.director} and the actors are {self.actors}.")

movie1 = Movie(
    'Topgun',
    120, 'action',
    'John Doe',
    ['actor1', 'actor2']
)

print(movie1.title)
print(movie1.duration)
print(movie1.genre)
print(movie1.actors)
movie1.show_details()
print("===================")
print(movie1.director)

movie1.director = "Nick Doe"
print(movie1.director)

del movie1.director
print(movie1.director)