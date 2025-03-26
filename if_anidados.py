'''
if anidados
if dentros de otros de otros iff

Syntax:
if condicion:
    if condicion:
        print("mensaje")
    else:
        print("mensaje")

no confundirr con elif  (if en condicion)

'''

#ejemplo1
#modifique de la edad   para las siguientes condiciones:
#1 si es mayor de 18 años pero no tiene doccumento no puede votar de lo contrario si puede votar
#2 si es menor de 18 años no puede votar
#utilice esstructura de if anidados

edad = int(input("Ingrese su edad:"))
if edad >= 18:
    documento = input ("Tiene documento? (si/no):")
    if documento == "si":
        print("Puede votar")
    else:
        print("No puede votar")
else:
    print("No puede votar")