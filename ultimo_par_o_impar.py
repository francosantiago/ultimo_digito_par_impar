"""PROGRAMA PARA
DE UN NUMERO DE CUATRO DIGITOS SABER SI SU ULTIMO ES PAR O IMPAR"""

print("------------------------------------")
print("----Ultimo digito es par o impar----")
print("------------------------------------")

# input

a = input("Ingrese el primer digito: ")
b = input("Ingrese el segundo digito: ")
c = input("Ingrese el tercer digito: ")
d = int(input("Ingrese el cuarto digito: "))

# processing

if d % 2 == 0:
    msj = " es par "
else:
    msj = " es impar "


# output

print("El ultimo digito del numero" + msj)

