# test_operaciones_comparacion.py
import unittest
from operaciones_comparacion import es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que, son_iguales


class TestOperacionesComparacion(unittest.TestCase):

    def test_es_mayor_que(self):
        #Casos Verdaderos: 
        self.assertGreater(es_mayor_que(6, 4), 0)

        # Casos Falsos 
        self.assertFalse(es_mayor_que(4, 6))
        self.assertFalse(es_mayor_que(6, 6))
        #Casos Falsos y probando dar un mensaje de error: 
        mensaje = "ERROR! El valor de a no es mayor que el valor de b"
        self.assertGreater(es_mayor_que(3, 9), 0, mensaje)
        self.assertTrue(es_mayor_que(1, 3), mensaje) 
        

    def test_es_menor_que(self):
        #Caso Verdadero
        self.assertLess(es_menor_que(5, 7), 3)      
        self.assertTrue(es_menor_que(0, 1))

        # Caso Falso
        self.assertFalse(es_menor_que(6, 4))
        self.assertFalse(es_menor_que(6, 6))

    def test_es_mayor_o_igual_que(self):
        # Casos Verdaderos
        self.assertTrue(es_mayor_o_igual_que(6, 4))
        self.assertTrue(es_mayor_o_igual_que(6, 6))
        self.assertGreaterEqual(es_mayor_o_igual_que(8, 8), 0)  # Otra forma de probar True

        # Retornar Falso 
        self.assertFalse(es_mayor_o_igual_que(4, 6))

    def test_es_menor_o_igual_que(self):
        # Casos a <= b - Casos Verdaderos 
        self.assertTrue(es_menor_o_igual_que(4, 6))
        self.assertTrue(es_menor_o_igual_que(6, 6))
        self.assertLessEqual(es_menor_o_igual_que(3, 3), 1)  # Otra forma de probar True

        # Casos Falsos
        self.assertFalse(es_menor_o_igual_que(6, 4))

    def test_son_iguales(self):
        mensaje = "ERROR! Los valores no son iguales"
        # Casos donde a y b son iguales
        self.assertTrue(son_iguales(8, 8))
        self.assertEqual(son_iguales(10, 10), True)
        #probando comparar floats con enteros
        self.assertEqual(son_iguales(12.00000000000000001, 12), True) #esto es verdadero
        self.assertEqual(son_iguales(12.000000000001, 12), True, mensaje) #esto es Falso, por lo tanto va a tener error
        

        # Casos donde a y b NO son iguales
        self.assertFalse(son_iguales(8, 9), mensaje)
        self.assertEqual(son_iguales(1, 3), False)

if __name__ == '__main__':
    unittest.main()
