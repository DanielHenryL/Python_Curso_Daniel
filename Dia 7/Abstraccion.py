'''La abstracción es el pilar de la programación orientada a objetos que se relaciona con ocultar toda la complejidad
que algo puede tener por dentro, ofreciendo una interfaz con funciones de alto nivel, por lo general sencillas de usar,
que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay dentro.

Piensa en cuántos objetos de ingeniería o aplicaciones utilizas en tu día a día, que tienen una interfaz sencilla y por
dentro un comportamiento complejo.

¿Qué sucedería si para poder conducir debiéramos conocer cada uno de los detalles de funcionamiento de un automóvil, desde
el giro de sus engranajes al circuito eléctrico que alimenta el mecanismo que sube y baja los vidrios de las ventanillas?
Para operar este último, un conducto solamente necesita accionar un botón y que el mismo realice la acción esperada.
Este botón abstrae al conductor de un sistema complejo y le proporciona una interfaz sencilla para lograr su objetivo.
Si lo programáramos, los métodos podrían ser subir() y bajar(), y en su interior, distribuir energía y accionar mecanismos
en los diferentes sectores del vehículo.

A esto mismo debe apuntar nuestro código: sin importar lo complejo que necesite ser en su interior,
una buena abstracción permite ofrecer métodos sencillos y de funcionamiento predecible de acuerdo con su denominación.'''