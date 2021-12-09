""""
Date:     2021-11-05
Authors:  Julio Cesar Rodriguez Castillo
File:     T1E1_pos_neg.py
Brief:    Programa que obtiene un numero entero o flotante y determina
          si es positivo,negativo o cero.
Score:    85
Version:  1.1.1
Fixes:    - PEP8 recomienda añadir espacios en blanco alrededor de
               los operadores
                
          - No se incluyó directorio Tarea_01 en el repositorio
"""

if __name__=='__main__':                          # PEP8
     print("Escribe un número entero: ")
     # Seria mejor castear a float para que el programa sea más vérsatil
     n = int(input())
     if n > 0:
          print("Número positivo")
     elif n < 0:
          print("Número negativo")
     else:
          print("El número que ingresaste es 0")
