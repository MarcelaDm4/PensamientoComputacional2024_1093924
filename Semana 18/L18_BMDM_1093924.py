# Ejercicio 1
#listaPrecios = [50, 75, 46, 22, 80, 65, 8]

#def menor(listaPrecios):
# listaPrecios.sort()
# return listaPrecios[0]



#def mayor(listaPrecios):
# listaPrecios.sort()
# listaPrecios.reverse()
# return listaPrecios[0]

#print("El precio mínimo es "+ str(menor(listaPrecios)))
#print("El precio máximo es "+ str(mayor(listaPrecios)))

#Ejercicio 2
#abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
#print(abc)

#for x in range(len(abc)-1,-1,-1):
#    if (x%3==0 and x!=0):
#        abc.pop(x)

#print(abc)

#Ejercicio 3
palabras = ['hola', 'banana', 'manzana', 'fresa', 'hola','fresa','hola','fresa','sandia','manzana']

encontrar = input('Escoja entre fresa, manzana, banano, hola, zapato, sandia: ')
contador = 0

for palabra in palabras:
    if palabra == encontrar:
       contador = contador+1

print("La palabra "+encontrar+" aparece "+str(contador)+" veces ")

 






    
