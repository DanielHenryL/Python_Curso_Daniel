class Padre:
    def hablar(self):
        print('hola')

class Madre:
    def reir(self):
        print('jajaja')

    def hablar(self):
        print('q tal')

class Hijo(Madre,Padre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
print(Nieto.__mro__)