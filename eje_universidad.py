estrato = int(input("Ingrese el estrato del estudiante (1 o 2): "))
edad = int(input("Ingrese la edad del estudiante: "))
valor_matricula = float(input("Ingrese el valor de la matrícula: "))



def calcular_descuento(estrato, edad, valor_matricula):
    if estrato == 1:
        if edad < 18:
            descuento = 0.20
        else:
            descuento = 0.15
    elif estrato == 2:
        if edad < 18:
            descuento = 0.10
        else:
            descuento = 0.05
    else:
        descuento = 0.00
    
    valor_descuento = valor_matricula * descuento
    valor_final = valor_matricula - valor_descuento

    return valor_final, valor_descuento


valor_final, valor_descuento = calcular_descuento(estrato, edad, valor_matricula)

    print(f"El valor del descuento es: ${valor_descuento:.2f}")
    print(f"El precio final de la matrícula es: ${valor_final:.2f}")