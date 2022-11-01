''' El acoplamiento es un concepto que mide la dependencia entre dos módulos distintos (como por ejemplo,
 clases). Podemos hablar de dos tipos:

Acoplamiento débil, que implica que no hay dependencia entre un módulo y otros. Esta es la situación ideal.
Acoplamiento fuerte, que es la situación contraria, e indica que el módulo tiene dependencias internas con otros.
Se trata de un pilar vinculado con la cohesión, ya que por lo general un acoplamiento débil se asocia a una cohesión fuerte.
Esta última es la situación buscada al escribir código.
Es decir, buscamos que una clase o función no tenga dependencias con otras clases o funciones,
y que las tareas que realizan estén relacionadas entre sí. Esto simplifica la lectura y mantenimiento del código,
a la vez que permite reutilizarlo en otros programas.

Para terminar de comprenderlo, imaginemos la situación contraria: un código fuertemente acoplado:

Si quisiéramos reutilizar un módulo que depende de otros, deberíamos “traer” también todas las dependencias,
de lo contrario resultaría en errores y pérdida de funcionalidad.
Si efectuamos un cambio en un módulo dependiente de otros, los efectos de este cambio pueden afectar a
los otros módulos que dependen del anterior.
Es muy importante prestarle atención a medida que nuestros programas crecen y se hacen más complejos,
donde este tipo de situaciones pueden comenzar a ocurrir inadvertidamente. Si esto sucede,
un cambio en una clase puede inutilizar otra, haciendo que deje de funcionar.
Una situación de acoplamiento fuerte puede originar errores que son difíciles de depurar.

Veamos el siguiente ejemplo:

class Mascota:
     tiene_patas = True
     pass
 class Perro:
     def correr(self, velocidad):
         if Mascota.tiene_patas:
             self.velocidad = velocidad
 mi_mascota = Perro()
 mi_mascota.correr("rápido")
 print(mi_mascota.velocidad)
Tenemos una clase Mascota que define un atributo de clase tiene_patas.
Por otra parte, la clase Perro basa el comportamiento del método correr() en el atributo tiene_patas de la clase Mascota.
Tenemos acoplamiento fuerte, ya que hay una dependencia entre la función de una clase con el atributo de otra.

Si tu programa debe contener dependencias externas, deberás asegurarte que las mismas son esenciales y
están debidamente justificadas para minimizar los efectos adversos mencionados.'''