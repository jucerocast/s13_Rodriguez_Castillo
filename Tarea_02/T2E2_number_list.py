"""
Date:       2021-11-17
Authors:    Julio Cesar Rodriguez Castillo
File:       
Brief:      
Score:      80
Version:    1.1.1
Fixes:      - Falto el encabezado (docstring)
            
            - PEP8 recomienda añadir un espacio en blanco después del
                carácter de almohadilla '#' de los comentarios
            
            - El paso 4 para ordenar esta comentado
"""

if __name__ == '__main__':
    Numeros = input('Escribe una serie de números: ').split(' ')
    #Imprimir elementos y tipo de lista
    print(Numeros)
    print(type(Numeros))

    #Cambiar el tipo de todos los elementos a int
    Lista = [int(x) for x in Numeros]
    print(Lista)

    # Imprimir elemento a través de valor ingresado por usuario
    Valor = int(input('Indique el valor que desea imprimir: '))
    if Valor in Lista:
        print(Valor)

    # Ordenar elementos
    #Lista.sort()
    #print(Lista)

    # Ordenar elementos a la inversa
    Lista.reverse()
    print(Lista)
