'''
if else:
deternina dos caminos de ejecución basados en la evaluación de una condicional

Sintaxis:

if condicional:
    instruccion1
    instruccion2
else:
    instruccion3
    instruccion4 
'''

#ejemplo
#elaboe un programa en python que determine si una persona es mayor o menor de edad y por tan tanto,habilitada para votar

edad = 21
documento = False

if edad >= 18 and documento==True:
    print("Usted es mayor de edad")
    print("Puede votar")
else:
    print("Usted es menor de edad")
    print("o")
    print("No puede votar")
print("Fin del programa")

