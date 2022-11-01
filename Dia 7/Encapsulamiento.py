'''El encapsulamiento es el pilar de la programación orientada a objetos que se relaciona con ocultar al exterior
determinados estados internos de un objeto, tal que sea el mismo objeto quien acceda o los modifique,
pero que dicha acción no se pueda llevar a cabo desde el exterior, llamando a los métodos o atributos directamente.

Si bien en algunos lenguajes (como Java), puede resultar un procedimiento habitual, Python no lo implementa por defecto,
pero nos propone una vía alternativa para lograrlo. Esto se hace anteponiendo dos guiones bajos (__)
al nombrar un método o atributo. De esa manera, los mismos quedarán definidos como “privados”,
y únicamente el mismo objeto podrá acceder a ellos.

class Persona:
    atributo_publico = "Mostrar"   # Accesible desde el exterior
    __atributo_privado = "Oculto"  # No accesible
    # No accesible desde el exterior
    def __metodo_oculto(self):
        print("Este método está oculto")
        self.__variable = 0
    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__metodo_oculto()

alumno = Persona()
# alumno.__metodo_oculto()  # Este método no es accesible desde el exterior
alumno.metodo_normal()      # Este método es accesible
Existe un pequeño truco (no recomendado) para acceder a los atributos y métodos ocultos.
Dichos métodos están presentes con un nombre algo distinto:

instancia + _ + NombreClase + método/atributo oculto

alumno._Persona__metodo_oculto()
print(alumno._Persona__atributo_privado)'''