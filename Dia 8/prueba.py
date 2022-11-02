import unittest
from cambia_texto import todo_mayusculas


class ProbarCambioTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = todo_mayusculas(palabra)
        self.assertEqual(resultado,palabra.upper())


if __name__ == '__main__':
    unittest.main()
