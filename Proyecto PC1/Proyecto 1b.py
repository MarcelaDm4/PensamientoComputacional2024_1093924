boletosR1=0
boletosR2=0
boletosR3=0
boletosR4=0
boletosR5=0
boletosT=0
ingresos=0
print("Bienvenidos al Transmetro")
while True:
 print("Selecciona el número del menú al que deseas seguir\n")
 print("1. Estaciones y rutas \n" 
 "2. Compra tus boletos \n"
 "3. Reportes \n" 
 "4. Salir\n")
 op= int(input()) 
 if op==4:
   print("Has salido del sistema. \nGracias por utilizar transmetro")
   break
 match op: 
      case 1:
        print("ESTACIONES")
        print("Código   Estación \n"
        "51       Estación Javier \n"
        "61       Estación Trébol \n"
        "71       Estación Don Bosco \n"
        "82       Estación Plaza Municipal")
        print("\nRUTAS")
        print("Ruta 1: 51 hacia 61 \n"
        "Ruta 2: 51 hacia 71 \n"
        "Ruta 3: 71 hacia 82 \n"
        "Ruta 4: 61 hacia 51 \n"
        "Ruta 5: 82 hacia 51 ")
        print("\nPresiona Enter para volver al menú y seguir la operación o, salir de ella.")
        input()
        print("\n")

      case 2:
        print("Ingresa tu nombre")
        nombre = input()
        print("Ingresa tu edad")
        edad = int(input())
        print("¿Estás embarazada?"
              "(Contesta 'si' o 'no' en minúsculas y sin tildes)")
        embarazo = input()
        if embarazo.isnumeric():
          print("Respuesta no reconocida. Intente de nuevo, contestando 'si' o 'no'")
          print("¿Estás embarazada?"
                "(Contesta 'si' o 'no' en minúsculas y sin tildes)")
          embarazo = input()

        
        print("Ingresa el número de ruta")
        ruta= int(input())
        
        match ruta:
          case 1:
            print("Su ruta parte de la estación Javier hacia la estación Trébol")
            km = 39
            precio = 1.50+((km-8)*0.25)
            if embarazo.lower() == 'si':
              precio = 0
              print("El boleto es gratis")
            elif 25 < edad > 15:
              precio = precio - (precio * 0.25)
              print("El costo de su boleto es de Q"+str(precio))
            else:
              print("El costo de su boleto es de Q" + str(precio))
            tiempo = km/20
            print("El tiempo aproximado del viaje será de "+str(tiempo)+"horas")
            boletosR1 += 1
            boletosT += 1
            ingresos +=precio
            print("\nPresiona Enter para seguir con la operación o para salir de ella.")
            input()
            print("\n")


        
          case 2:
            print("Su ruta parte de la estación Javier hacia la estación Don Bosco")
            km = 18
            precio = 1.50+((km-8)*0.25)
            if embarazo.lower() == 'si':
               precio = 0
               print("El boleto es gratis")
            elif 15<=edad<=25:
                precio = precio-(precio*0.25)
                print("El costo de su boleto es de Q"+str(precio))
            else: 
                print("El costo de su boleto es de Q"+str(precio))
            tiempo = km/20
            print("El tiempo aproximado del viaje será de "+str(tiempo)+"horas")
            boletosR2 += 1
            boletosT += 1
            ingresos += precio
            print("\nPresiona Enter para seguir con la operación o para salir de ella.")
            input()
            print("\n")



          case 3:
            print("Su ruta parte de la estación Don Bosco hacia la estación Plaza Municipal")
            km = 23
            precio = 1.50+((km-8)*0.25)
            if embarazo.lower() == 'si':
               precio = 0
               print("El boleto es gratis")
            elif 15<=edad<=25:
                precio = precio-(precio*0.25)
                print("El costo de su boleto es de Q"+str(precio))
            else: 
                print("El costo de su boleto es de Q"+str(precio))
            tiempo = km/20
            print("El tiempo aproximado del viaje será de "+str(tiempo)+"horas")
            boletosR3 += 1
            boletosT += 1
            ingresos += precio
            print("\nPresiona Enter para seguir con la operación o para salir de ella.")
            input()
            print("\n")


        
          case 4: 
            print("Su ruta parte de la estación Don Bosco hacia la estación Javier")
            km = 8
            precio = 1.50+((km-8)*0.25)
            if embarazo.lower() == 'si':
               precio = 0
               print("El boleto es gratis")
            elif 15<=edad<=25:
              precio = precio-(precio*0.25)
              print("El costo de su boleto es de Q"+str(precio))
            else: 
              print("El costo de su boleto es de Q"+str(precio))
            tiempo = km/20
            print("El tiempo aproximado del viaje será de "+str(tiempo)+"horas")
            boletosR4 += 1
            boletosT += 1
            ingresos += precio
            print("\nPresiona Enter para seguir con la operación o para salir de ella.")
            input()
            print("\n")


        
          case 5: 
              print("Su ruta parte de la estación Plaza Municipal hacia la estación Javier")
              km = 42
              precio = 1.50+((km-8)*0.25)
              if embarazo.lower() == 'si':
                 precio = 0
                 print("El boleto es gratis")
              elif 15<=edad<=25:
                precio = precio-(precio*0.25)
                print("El costo de su boleto es de Q"+str(precio))
              else: 
                print("El costo de su boleto es de Q"+str(precio))
              tiempo = km/20
              print("El tiempo aproximado del viaje será de "+str(tiempo)+"horas")
              boletosR5 += 1
              boletosT += 1
              ingresos += precio
              print("\nPresiona Enter para seguir con la operación o para salir de ella.")
              input()
              print("\n")

          case _:
              print("No existe esa ruta, ingrese una opción válida")
              print("\nPresiona Enter para volver al menú e intentar de nuevo.")
              input()
              print("\n")
        
      case 3:
        print("REPORTE")
        print("Se han comprado ",boletosR1," boletos para la ruta 1.\n"
              "Se han comprado ",boletosR2," boletos para la ruta 2.\n"
              "Se han comprado ",boletosR3," boletos para la ruta 3.\n"
              "Se han comprado ",boletosR4," boletos para la ruta 4.\n"
              "Se han comprado ",boletosR5," boletos para la ruta 5.\n"
              "Se han comprado ",boletosT," boletos en total.")
        print("La compra ha sido de Q"+str(ingresos))
        print("\nPresiona Enter para volver al menú.")
        input()
        print("\n")

        
           
      case _:
        print("Ingresa una opción válida")