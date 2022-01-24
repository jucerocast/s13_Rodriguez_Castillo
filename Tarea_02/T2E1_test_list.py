"""
Date:       2021-11-17
Authors:    Julio Cesar Rodriguez Castillo
File:       
Brief:      
Score:      80
Version:    1.1.1
Fixes:      - Falto el encabezado (docstring)
            
            - PEP8 recomienda no rebasar los 99 carácteres en una línea 
                de código, yo establecí en los requerimientos máximo 72
                carácteres (aplica para comentarios también)
            
            - PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','
            
            - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores, excepto en los paramétros
"""

if __name__ == '__main__':
    myList = ["Aristóteles", "Hegel", "Kant", "Kierkegaard", "Nietzsche", "Platón"]

    # Método append
    myList.append("Cicerón")
    print(myList)

    # Método insert
    myList.insert(3,"Fichte")
    print(myList)

    # Método pop
    myList.pop(5)
    print(myList)

    # Ordenar lista de la A a la Z
    myList.sort()
    print(myList)

    # Ordenar lista de la Z a la A
    myList.sort(reverse = True)
    print(myList)
