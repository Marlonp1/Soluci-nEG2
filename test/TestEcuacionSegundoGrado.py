import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):

    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

    def tearDown(self):
        self.calculoRaices = None

    def test_calculoESG_dosNumeros_retornaSolucion(self):

        # Arrange
        a = 3
        b = -5
        c = 1
        retultadoEsperadoRaiz1 = 1.43
        retultadoEsperadoRaiz2 = 0.23
        # Act
        resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.calculoESG(a,b,c)
        # Assert
        self.assertAlmostEqual(resultadoActualRaiz1,retultadoEsperadoRaiz1, places=2)
        self.assertAlmostEqual(resultadoActualRaiz2,retultadoEsperadoRaiz2, places=2)

if __name__ == '__main__':
    unittest.main()

