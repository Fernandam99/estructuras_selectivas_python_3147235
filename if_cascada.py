'''
if en cascada es una estructura selectiva compuesta por multiples codicionales
segidos unos de otros

if condicional1:
    instruccion1
    instruccion2
elif condicional2
     instruccion3
     instruccion4
elif condicional3
     instruccion5
     instruccion6

     
NOTA: cada condicional es mutuamente EXCLUYENTE
'''
#Vamos a hacer un pequeño traductor.
#el programa debe permitir lee una furta enespañol y debe 

fruta_es = input("ingrese fruta:")
if  fruta_es == "manzana" or fruta_es == "Manzana":
    print("apple")

elif fruta_es == "naranja" or fruta_es == "Naranja":
    print("orange")

elif fruta_es == "uva" or fruta_es == "Uva":
    print("grape")

elif fruta_es == "piña" or fruta_es == "Piña":
    print("pineapple")

#caso por defecto

else:
    print ("No se encontro traducción")