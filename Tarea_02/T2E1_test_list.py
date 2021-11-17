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