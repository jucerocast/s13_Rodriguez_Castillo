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