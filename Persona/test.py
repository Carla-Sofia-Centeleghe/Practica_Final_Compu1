import unittest
from persona import Persona, MenorEdadException


class TestFinal(unittest.TestCase):

    def test_creacion_persona(self):
        persona = Persona('Steve', 'Rogers', 25)
        self.assertEqual(persona.nombre, 'Steve')
        self.assertEqual(persona.apellido, 'Rogers')
        self.assertEqual(persona.edad, 25)

    def test_menor_edad_exception_1(self):  #final 02/08/2023
        with self.assertRaises(MenorEdadException):
            Persona('Star', 'Fire', 10)

    def test_menor_edad_exception_2(self): #final 20/09/2023
        with self.assertRaises(MenorEdadException):
           Persona('Natasha', 'Romanof', 17)

if __name__ == '__main__':
    unittest.main()