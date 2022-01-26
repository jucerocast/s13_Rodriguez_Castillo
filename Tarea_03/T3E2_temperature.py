"""
Date:       2021-11-19
Authors:    Julio Cesar Rodriguez Castillo
File:
Brief:
Score:      80 (65)
Version:    0.1.1
Fixes:      * Las funciones se deben declarar antes del la condicion
                de if __name__ == '__main__':

            - [10] PEP8 recomienda que cada declaración de función debe
                tener 2 lineas en blanco arriba y abajo, si se les agrega
                un comentario arriba entonces las 2 lineas en blanco deben
                estar encima del comentario.

            - [20] PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','

            - [5] No tiene docstring el archivo (encabezado)
"""


if __name__ == '__main__':
    #Funcion de conversión centígrados a fahrenheit
    def funcion_cenfa(x):
       return ((x * (9 / 5)) + 32)
    resultado1 = funcion_cenfa(1)
    resultado2 = funcion_cenfa(10)
    resultado3 = funcion_cenfa(18)
    print(round(resultado1,2),'grados fahrenheit')
    print(round(resultado2, 2), 'grados fahrenheit')
    print(round(resultado3, 2), 'grados fahrenheit')


    # Funcion de conversión fahrenheit a centígrados
    def funcion_facen(y):
        return (y - 32) * 5 / 9
    resultado4 = funcion_facen(1)
    resultado5 = funcion_facen(10)
    resultado6 = funcion_facen(18)
    print(round(resultado4,2),'grados centígrados')
    print(round(resultado5, 2), 'grados centígrados')
    print(round(resultado6, 2), 'grados centígrados')
