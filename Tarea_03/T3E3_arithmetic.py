"""
Date:       2021-11-19
Authors:    Julio Cesar Rodriguez Castillo
File:
Brief:
Score:      80 (75)
Version:    1.1.1
Fixes:      * La funciones se debe declarar antes del la condicion
                de if __name__ == '__main__':

            - [20] PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','

            - [5] No tiene docstring el archivo (encabezado)

            * En los return no hace falta paréntesis
"""


if __name__ == '__main__':
    #función de suma
    def fun_suma(x,y):
        return (x+y)
    resultado = fun_suma(7,9.65)
    resultado1 = fun_suma(3.1416, 90)
    print(resultado)
    print(resultado1)

    #función de resta
    def fun_resta(x,y):
        return (x-y)
    resultado = fun_resta(459.23, 210.66)
    resultado1 = fun_resta(45.9, 53.6)
    print(resultado)
    print(resultado1)

    #función de multiplicar
    def fun_multi(x,y):
        return(x*y)
    resultado = fun_multi(20,15)
    resultado1 = fun_multi(12,50)
    print(resultado)
    print(resultado1)

    #función de división
    def fun_div(x,y):
        return(x/y)
    resultado = fun_div(25,5)
    resultado1 = fun_div(10,3)
    print(resultado)
    print(resultado1)
