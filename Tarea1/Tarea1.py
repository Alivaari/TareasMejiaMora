from num2words import num2words  # importa la libreria de num2words


def string_work(palabra):
    if isinstance(palabra, str):  # Comprueba si la variable de la funcion
        # es un string
        if palabra.isalpha():  # Comprueba si la variable de la funcion
            # esta conformada por letras unicamente
            output = palabra.swapcase()  # Funcion que invierte las
            # mayusculas y minusculas de un string
        else:
            output = 2  # Error 2, el parametro contiene caracteres
            # que no son letras
    else:
        output = 1  # Error 1, el parametro no es un string
    return output


def num_to_str(numero):
    if isinstance(numero, str):  # Comprueba si el parametro de la funcion
        # es un string
        output2 = 3  # Error 3, el parametro es un string
    else:
        if 99 >= numero & numero >= 0 & isinstance(numero, int):  # Comprueba
            # si el parametro es un numero entero positivo entre 0 y 99
            numero = num2words(numero, lang='es')  # Instruccion que traduce un
            # numero entero a string en español
            output2 = numero.replace(" ", "_")  # Instruccion que reemplaza
            # los espacios en blanco por _
        else:
            output2 = 4  # Error 4, el parametro es un numero negativo,
            # decimal o mayor a 99
    return output2
