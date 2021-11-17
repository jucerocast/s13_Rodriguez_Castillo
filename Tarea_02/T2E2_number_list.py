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