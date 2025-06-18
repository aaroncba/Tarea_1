# Tarea_1
Probando unittest

Leyendo mas informacion sobre unittest en diferentes sitios, como en la [documentacion](https://docs.python.org/3/library/unittest.html#assert-methods) que ofrece python y [geeksforgeekts.org](https://www.geeksforgeeks.org/python/python-unittest-assertfalse-function/), note que se pueden hacer cosas como agregar un mensaje en caso que el test falle. Como por ejemplo: 
```
======================================================================
FAIL: test_es_mayor_que (__main__.TestOperacionesComparacion)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\UNAH\PAC II\POO\Tare_1\test_operaciones_comparacion.py", line 17, in test_es_mayor_que
    self.assertGreater(es_mayor_que(2, 8), 0, mensaje)
AssertionError: False not greater than 0 : ERROR! El valor de a no es mayor que el valor de b

======================================================================
```
