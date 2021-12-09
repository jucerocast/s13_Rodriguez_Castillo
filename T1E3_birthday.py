""""
Date:     2021-11-05
Authors:  Julio Cesar Rodriguez Castillo
File:     T1E3_birthday.py
Brief:    Programa que que imprime una cadena correspondiente a una 
          fecha de cumpleaños
Score:    35
Version:  0.1.1
Fixes:    - EL código no realiza la función deseada

          - PEP8 recomienda añadir espacios en blanco alrededor de
               los operadores
                
          - No se incluyó directorio Tarea_01 en el repositorio
"""

if __name__=='__main__':                          # PEP8
     print("Escribe un número entero: ")
     n = int(input())
     if n > 0:
          print("Número positivo")
     elif n < 0:
          print("Número negativo")
     else:
          print("El número que ingresaste es 0")
