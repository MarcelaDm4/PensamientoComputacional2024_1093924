# Ejercicio 1
print("Ingrese su edad")
edad= int(input())
if edad >= 18:
    print("Es necesario que tramite su DPI")
else:
    print("Es menor de edad, aún no necesita DPI")

# Ejercicio 2
print("Ingrese un número")
num= int(input())
if num>=0:
    print("Su número es positivo")
else:
    print("Su número es negativo")

# Ejercicio 3
print("Ingrese un número del 1 al 5")
numero = int(input())
numero == 1 
match numero:
    case 1:
        print("uno")
    case 2:
        print("dos")
    case 3:
        print("tres")
    case 4:
        print("cuatro")
    case 5:
        print("cinco")
    case _:
        print("Número no definido")

# Ejercicio 4
print("A continuaión se presenta la tabla del 2")
c=0
while c<=10:
    x=c*2
    print("2x" +str(c)+ "= "+str(x))
    c=c+1
    
