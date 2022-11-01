class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice muuuu')


class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice meee')

vaca1 = Vaca('Lola')
oveja1 = Oveja('dora')

#Iterar
animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()

#Mediante funcion
def animal_hablar(animal):
    animal.hablar()

animal_hablar(oveja1)