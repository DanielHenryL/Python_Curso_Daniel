#### Herencia ####
class Animal:

    #atrbutos de instancia
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    #Metodos de instancia
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    #Agregar atributos de instancia a la clase hija
    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('pio')

    def volar(self):
        print(f'El pajaro vuela {self.altura_vuelo} metros')

piolini = Pajaro(2,"amarillo",100)
piolini.hablar()
piolini.volar()