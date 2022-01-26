"""
Date:       2021-11-19
Authors:    Julio Cesar Rodriguez Castillo
File:
Brief:
Score:      80
Version:    1.1.1
Fixes:      * La funcion se debe declarar antes del la condicion
                de if __name__ == '__main__':
                por lo mismo hay un warning con la variable numero

            - [5]  No puedes asignar a la variable numero el resultado
                de print porque print no retorna nada.

            - [5] No tiene docstring el archivo (encabezado)
            
            - [10] Si bien en la terminal hace lo que se pide,
                la funcion no debe llamarse a si misma, a eso
                se le llama recursividad, pero en este caso
                no es lo que se solicito.
"""


if __name__ == '__main__':
    numero = print(float(input("Escribe un número: ")))

    def my_function(numero):
        my_function(str(numero))
        print(my_function())
