import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):

    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

    def tearDown(self):
        self.calculoRaices = None

    def test_calculoESG_dosNumeros_retornaSolucion(self):

        # Arrange
        a = 1
        b = 2
        c = 1
        retultadoEsperadoRaiz1 = -1
        retultadoEsperadoRaiz2 = -1
        # Act
        resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.calculoESG(a,b,c)
        # Assert
        self.assertEqual(resultadoActualRaiz1,retultadoEsperadoRaiz1)  # add assertion here
        self.assertEqual(resultadoActualRaiz2, retultadoEsperadoRaiz2)

if __name__ == '__main__':
    unittest.main()

