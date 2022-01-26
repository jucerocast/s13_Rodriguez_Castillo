"""
Date:       2022-01-19
Author:     Julio César Rodríguez Castillo
File:       _init_.py
Brief:      Validación de correo, teléfono y CURP mediante expresiones regulares
Score:
Version:    0.0.1
"""

from paqueteT2.validadExp import *

if __name__== '__main__':
    resultado = ("inválido", "válido")
    print("\nIntroduce tu correo: ", end=' ')
    correo = input()

    print ("Introduce tu número de teléfono: ", end=' ')
    telefono = input()

    print("Introduce tu CURP: ", end=' ')
    curp = input()

    print(f"\nEl correo {correo} es {resultado[validaCorreo(correo)]}")
    print(f"El número de teléfono {telefono} es {resultado[validaTel(telefono)]}")
    print(f"El CURP {curp} es {resultado[validaCURP(curp)]}")