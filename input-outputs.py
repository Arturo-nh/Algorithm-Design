import math
#Ejrecicio No 1
def calculate_age_in_fifteen_years():
    edad = int(input("Escribe tu edad:"))
    Futuro = edad + 15
    print("Tu edad en 15 años sera", Futuro)

#Ejercicio No 2
def previous_number():
    num = int(input("Escribe un numero entero: "))
    answr = num-1
    print("El numero anterior es",answr)

#Ejercicio No 3
def doble_and_half():
    num = int(input("Escribe un numero entero: "))
    doble = num * 2
    mitad = float(num/2)
    print("El doble de tu numero es",doble,"y la mitad de tu numero es",mitad)

#Ejercicio No 4
''''
num1 = int(input("Escribe el primer numero entero: "))
num2 = int(input("Escribe el segundo numero entero: "))
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = float(num1/num2)
print("Resultados:")
print("Suma:",suma)
print("Resta:",resta)
print("Multiplicacion",mult)
print("Divicion:",round(div,2))
'''

#Ejercicio No 5
'''
centenas=int(input("Introduce cualquier numero mayor a 100:"))
answr=centenas//100
print("Tu numero tiene",answr,"centenas")
'''

#Ejercicio No 6
'''
decenas=int(input("Introduce cualquier numero entero: "))
answr=(decenas//10)%10
print("El numero de las decenas es",answr)
'''
#Ejercicio No 7

#Ejercicio No 8
'''
palabra=input("Escribe una palabra: ")
print("("+palabra+")")
'''

#Ejercicio No 9

# pal1=str(input("Ingresa la primera palabra: "))
# pal2=str(input("Ingresa la segunda palabra: "))
# answr=pal1+ " " +pal2
# print(answr)


#Main
# calculate_age_in_fifteen_years

###############################################################################################################################

def decompose_number():
    num=int(input("Introduce un numero natural entre 100 y 999: "))
    cent=num//100
    dec=(num//10)%10
    uni1=int(str(cent)+str(dec)+str(0))
    uni2=num-uni1
    print(cent)
    print(dec)
    print(uni2)

    # decomposed = list(str(num))
    # print(decomposed)

# Ejercicio 2 p2
def repeticion_de_letra():
    letra=input("Escribe cualquier letra: ")
    num=int(input("Escribe un numero:" ))
    cadena=letra * num
    print(cadena)

def pair_of_points():
    x1=int(input("Escribe x1: "))
    y1=int(input("Escribe y1: "))
    x2=int(input("Escribe x2: "))
    y2=int(input("Escribe y2: "))

    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("La distancia entre los dos puntos es: ",d)

# decompose_number()
# pair_of_points()
repeticion_de_letra()
