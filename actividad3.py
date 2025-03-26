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

=> para el caso de prestacio de servicios
    se debe solicitar:
    -El valor del contrato
    -El numero de meses del contrato
    -La antiguedad del empleado (años)
El salario neto, en este caso se clacula:
1. dividir el valor del contrato por el numero de meses
2. restar el 15% del valor del contrato por concepto de EPS
3. restar el 15% del valor del contrato, por concepto de pension
4. si el empleado tiene una antiguedad igual o superior a 10 tendra una bonificacion del 0.5% 
sobre el salario mensual

=> para el caso del contrato a termino indefinido se debe solicitar:
    -antiguedad(años)
    -grado o escalafon (1 - 5)
    -El valor del salario minimo

El salrio neto  calcula de acuerdo a la siguiente tabla:
 -grado 1: 1.5 SM
 -grado 2: 1.5 SM
 -grado 3: 1.5 SM
 -grado 4: 1.5 SM
 -grado 5: 1.5 SM

 La bonificacion estara acorde as los siguientes rangos segun la antiguedad
 antiguedad:
 -entre 1 y 5 años 1% de salario mensual
 -entre 1 y 10 años 2% de salario mensual
 -superior a 20 años 3% de salario mensual
 
 para este aso los descuentos de ley son:
 -20% por eps
 -22% por pension
 -0.1% por ARL
'''
contrato = input  ("Ingrese el tipo de contrato:")
#inicializar variables:
#dar vaalor inicial a una variable asi no se utilice en el momento
salario_neto = 0

if contrato == "a":
    print("Eligió: Contrato a termino indefinido ")
    antiguedad = int(input("Ingrese antiguedad del empleado(años):"))
    grado = int(input("Ingrese grado o escalafon(1-5):"))
    salario_minimo = int(input("Ingrese valor del salario minimo:"))
    salario_mensual = 0
    if grado == 1:
        salario_mensual = salario_minimo * 1.5
    elif grado == 2:
        salario_mensual = salario_minimo * 1.7
    elif grado == 3:
        salario_mensual = salario_minimo * 2.0
    elif grado == 4:
        salario_mensual = salario_minimo * 2.5  
    elif grado == 5:
        salario_mensual = salario_minimo * 3.0
    ##calcular bonificacion
    bonificacion = 0
    if antiguedad >= 1 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.01
    if antiguedad > 5 and antiguedad <= 10:
        bonificacion = salario_mensual * 0.02
    if  antiguedad > 10:
        bonificacion = salario_mensual * 0.03
    ##descuentos de ley
    eps = salario_mensual * 0.25
    pension = salario_mensual * 0.22    
    arl = salario_mensual * 0.001  
    salario_neto = salario_mensual - eps - pension - arl + bonificacion

elif contrato == "b":
    print("Eligio: Contrato por prestacion de sericios")
    valor_contrato = int(input("Ingrese valor del contrato: "))
    numero_meses = int(input("Ingrese el numero de meses del contrato: "))
    antiguedad = int(input("Ingrese el numero de años del contrato:"))
    salario_mensual = valor_contrato / numero_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.05
    salario_neto = salario_mensual - eps - pension
    if antiguedad >= 10:
        salario_neto = salario_neto + bonificacion
    print ("El salario neto es ", salario_neto)


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


    
    