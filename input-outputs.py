import math
import cmath
#Ejercicio No 1
def calculate_age_in_fifteen_years():
    edad = int(input("Escribe tu edad:"))
    Futuro = edad + 15
    print("Tu edad en 15 años sera", Futuro)

#calculate_age_in_fifteen_years()

#Ejercicio No 2
def previous_number():
    num = int(input("Escribe un numero entero: "))
    answr = num-1
    print("El numero anterior es",answr)

#previous_number()

#Ejercicio No 3
def doble_and_half():
    num = int(input("Escribe un numero entero: "))
    doble = num * 2
    mitad = float(num/2)
    print("El doble de tu numero es",doble,"y la mitad de tu numero es",mitad)

#doble_and_half()

#Ejercicio No 4
def basic_operations():
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

#basic_operations()


#Ejercicio No 5
def centenas():
    centenas=int(input("Introduce cualquier numero mayor a 100:"))
    answr=centenas//100
    print("Tu numero tiene",answr,"centenas")

#centenas()


#Ejercicio No 6
def decenas():
    decenas=int(input("Introduce cualquier numero entero: "))
    answr=(decenas//10)%10
    print("El numero de las decenas es",answr)

#decenas()

#Ejercicio No 7
def next_even_number():
    num=int(input("Escribe un numero entero: "))
    answr=num+2-(num%2)
    print("El siguiente numero par es",answr)

#next_even_number()

#Ejercicio No 8
def print_word_in_parentheses():
    palabra=input("Escribe una palabra: ")
    print("("+palabra+")")

#print_word_in_parentheses()

#Ejercicio No 9
def concatenate_two_words():
    pal1=str(input("Ingresa la primera palabra: "))
    pal2=str(input("Ingresa la segunda palabra: "))
    answr=pal1+pal2
    print(answr)

#concatenate_two_words()

#Ejercicio No 10
def capital_and_lowercase():
    palabra=input("Escribe una palabra: ")
    print(palabra.upper())
    print(palabra.lower())

#capital_and_lowercase()

###############################################################################################################################

# Ejercicio 1 p2
def decompose_number():
    num=int(input("Introduce un numero natural entre 100 y 999: "))
    cent=num//100
    dec=(num//10)%10
    uni1=int(str(cent)+str(dec)+str(0))
    uni2=num-uni1
    print("Centenas: ",cent)
    print("Decenas: ",dec)
    print("Unidades:",uni2)      

#decompode_number()
    # decomposed = list(str(num))
    # print(decomposed)

#decompose_number()


###############################################################################################################################

# Ejercicio 2 p2
def repeticion_de_letra():
    letra=input("Escribe cualquier letra: ")
    num=int(input("Escribe un numero:" ))
    cadena=letra * num
    print(cadena)

#repeticion_de_letra()
    
###############################################################################################################################
# Ejercicio 3 p2
def square_root_of_a_number():
    num=int(input("Escribe un numero entero: "))
    answr=math.sqrt(num)
    print("El cuadrado de tu numero es: ",answr)

#square_root_of_a_number()

###############################################################################################################################
# Ejercicio 4 p2
def formula_general():
    a=int(input("Escribe el numero real de a: "))
    b=int(input("Escribe el numero real de b: "))
    c=int(input("Escribe el numero real de c: "))
    disc=b**2-4*a*c
    answr1=(-b+(cmath.sqrt(disc)))/(2*a)
    answr2=(-b-(cmath.sqrt(disc)))/(2*a)

    print("La solucion de x1 es: ",answr1)
    print("La solucion de x2 es: ",answr2)

#formula_general()

###############################################################################################################################
# Ejercicio 5 p2
def pair_of_points():
    x1=int(input("Escribe x1: "))
    y1=int(input("Escribe y1: "))
    x2=int(input("Escribe x2: "))
    y2=int(input("Escribe y2: "))

    pmedio=( (x1+x2)/2 , (y1+y2)/2 )
    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("La distancia entre los dos puntos es: ",d)
    print("El punto medio entre los dos puntos es: ",pmedio)

pair_of_points()

