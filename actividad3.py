'''
Elabore un programa que permita calcular el salario neto de un empleado, despues de descontar los 
decuentos por conceptos de: salud, pension, ARL
1. el programa debe solicitar el tipo de empleado:
a-contratato a termino indefinido
b-contrato por prestacion de servicios
c-contrato de aprendizaje
d-contrato por jornal (freelance)

=> para el caso de jornal se debe soliciar el umero de horas trabajadas y el valor a pagar por hora
El total del salario se cacula de multiplicar el numero de horas por el valor a pagar por hora
'''
contrato = input  ("Ingrese el tipo de contrato:")
#inicializar variables:
#dar vaalor inicial a una variable asi no se utilice en el momento
salario_neto = 0

if contrato == "a":
    print("Eligio: Contrato a termino indefinido")
elif contrato == "b":
    print("Eligio: Contrato por prestacion de sericios")
elif contrato == "c":
    print("Eligio: Contrato de aprendizaje")
    salario_minimo = int(input("Ingrese el valor del salario minimo"))
    salario_neto = salario_minimo * (salario_minimo * 0.25)
    print("El salario neto es: ", salario_neto)
elif contrato == "d":
    print("Eligio: Contrato por jornal")
    #variable local:
    #es una variable que solo se puede utilizar en un bloque
    #por lo tanto solo se puede ustilizar en un bloque
    numero_horas = int(input ("Ingrese el numero de horas:"))
    valor_hora = int(input ("Ingrese el valor por hora:"))
    salario_neto = numero_horas * valor_hora
    print ("El salario neto es: ", salario_neto)
else:
    print ("Tipo de contrato no existente")
print("Fin del programa")


    
    