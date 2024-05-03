# Ejercicio 1
print("Ingrese medida del lado 1:")
Lado1 = int(input())
print("Ingrese medida del lado 1:")
Lado2 = int(input())
print("Ingrese medida del lado 1:")
Lado3 = int(input())

def triangulo(a,b,c):
    if a==b and b==c:
        return "Equilátero"
    elif a!=b and b!=c:
       return "Escaleno"
    else:
        return "Isósceles"

print("El triángulo es: "+ triangulo(Lado1,Lado2,Lado3))

# Ejercicio 2
import math  

print("Ingrese el radio del círculo")
radio = int(input())

def OBTperímetro(r):
    perímetro = float(2*r)*math.pi
    return perímetro

def OBTarea(r):
    area = float(r**2)*math.pi
    return area

def OBTvolumen(r):
    volumen = (4*math.pi*radio**3)/3
    return volumen

print("El perímetro de su círculo es: " + str(OBTperímetro(radio)))
print("El área de su círculo es: " + str(OBTarea(radio)))
print("El volumen de su círculo sería: " + str(OBTvolumen(radio)))

# Ejercicio 3
print("Ingrese un número del 1 al 12")
numero = int(input())

def mes(num):
    if num == 1:
      return "enero"
    elif num == 2:
       return "febrero"
    elif num == 3:
       return "marzo"
    elif num == 4:
       return "abril"
    elif num == 5:
       return "mayo"
    elif num == 6:
       return "junio"
    elif num == 7:
       return "julio"
    elif num == 8:
       return "agosto"
    elif num == 9:
       return "septiembre"
    elif num == 10:
       return "octubre"
    elif num == 11:
       return "noviembre"
    elif num == 12:
       return "diciembre"
    else:
       return "no válido"

print("Su número corresponde al mes de: " + mes(numero))