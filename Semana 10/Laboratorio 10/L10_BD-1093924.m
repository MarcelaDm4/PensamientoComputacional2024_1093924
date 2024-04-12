# Ejercicio 1
print("Ingrese un número")
num=int(input())
contador=1
producto=0
for contador in range(1,11):
    producto=num*contador
    print(str(contador)+"x"+str(num)+" = "+str(producto))
    contador=contador+1

# Ejercicio 2
print("Ingrese un número")
num=int(input())
contador=1
Cdivision=0
while contador<=num:
    if num%contador==0:
       contador=contador+1
       Cdivision=Cdivision+1

if Cdivision<=2:
   print("Su número es primo")
else:
   print("Su número es compuesto")

# Ejercicio 3
print("Ingrese un número")
num=int(input())
sum=1
total=0
for sum in range(1,num):
    total=sum+(sum+1)
    sum=total
print("La suma de los números hasta "+str(num)+" es igual a "+str(total))