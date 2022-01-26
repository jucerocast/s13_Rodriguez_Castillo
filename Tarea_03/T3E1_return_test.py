"""
Date:       2021-11-19
Authors:    Julio Cesar Rodriguez Castillo
File:       
Brief:      
Score:      45
Version:    0.1.1
Fixes:      - La funcion se debe declarar antes del la condicion
                de if __name__ == '__main__':

            - No puedes asignar a la variable numero el resultado
                de print porque print no retorna nada

            - [50] El programa no funciona
            
            - [5] No tiene docstring el archivo (encabezado)
"""


if __name__ == '__main__':
    numero = print(float(input("Escribe un número: ")))

    def my_function(numero):
        my_function(str(numero))
        print(my_function())
