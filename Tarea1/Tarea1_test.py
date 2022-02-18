from num2words import num2words
from Tarea1 import string_work
from Tarea1 import num_to_str


def test_string_work_swap():  # Funcion para realizar el test de
    # inversion de mayusculas y minusculas de un string
    a = "aAaA"  # Define el string a invertir
    assert(string_work(a) == a.swapcase())  # Assert que verifica que
    # se realiza la inversion de forma correcta


def test_string_work_err1():  # Funcion para realizar el test de
    # fallo si se introduce un numero como parametro
    a = 99  # Define el parametro como un entero
    assert(string_work(a) == 1)  # Assert que verifica que
    # se obtiene el error correspondiente


def test_string_work_err2():  # Funcion para realizar el test de
    # fallo si se tienen caracteres distintos a letras
    a = "aAaA6"  # Define el parametro como una combinacion de
    # numeros y letras
    assert(string_work(a) == 2)  # Assert que verifica que
    # se obtiene el error correspondiente


def test_num_to_str():  # Funcion para realizar el test de
    # comprobacion de traduccion de todos los numeros en el rango
    for i in range(100):
        a = num2words(i, lang='es')  # Instruccion que traduce los
        # numeros en el rango para compararlos
        a = a.replace(" ", "_")  # Reemplaza los espacios en blanco
        assert(num_to_str(i) == a)  # Assert que verifica que se
        # realiza la traduccion de forma correcta


def test_num_to_str_err3():  # Funcion para realizar el test de
    # fallo si se introduce un string
    a = "a"  # Define el parametro como un string
    assert(num_to_str(a) == 3)  # Assert que verifica que se
    # obtiene el error correspondiente


def test_num_to_str_err4():  # Funcion para realizar el test de
    # fallo si se introduce un numero fuera del rango o decimal
    a = 999  # Define el parametro como un numero fuera del rango
    assert(num_to_str(a) == 4)  # Assert que verifica que se
    # obtiene el error correspondiente
