import datetime 

horarios = {}
sensores=[]

def validate_time(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

print("Ha ingresado al sistema de automatización de temperatura HSmart\n")

# Se hace la configuración principal del sistema
print("El sistema le permite configurar y controlar la temperatura de 4 áreas de su preferencia \n")
print("Configure sus sensores\nIngrese el nombre del área")

for i in range(1, 5):
    while True:
        nombre = input(f"Ingresa el nombre para el área {i}: ")
        if not nombre.isnumeric():
            break
        print("Ingrese el nombre del área, no números.")
    numero = i  # Asignar el número del área automáticamente
    temperatura = 22
    sensores.append({"numero": numero, "nombre": nombre, "temperatura": temperatura})
print("Se han configurado sus áreas")

# Se abre la opción de menú para que el usuario escoja
while True:
    print("\nIngrese el número de menú al que desea continuar")
    print("1. Control de temperaturas\n"
          "2. Programación de horarios\n"
          "3. Sensores de temperatura\n"
          "4. Salir") 

    try:
        menu = int(input()) 
    except ValueError:
        print("Opción inválida. Por favor intenta de nuevo.")
        continue

    if menu == 4:
        print("Has salido del sistema")
        break 

    match menu:
        case 1:
            print("Configuración de temperaturas \n")
            for sensor in sensores:
                print(f"Número: {sensor['numero']}, Área: {sensor['nombre']}, Temperatura: {sensor['temperatura']}")

            # El usuario luego de verificar decide si quiere ajustar los sensores, cuáles y a qué temperatura
            print("\n¿Desea modificar algún sensor? (si o no)")
            res = input().strip().lower()
            if res not in ['si', 'no']:
                print("Respuesta no reconocida. Intente de nuevo, contestando 'si' o 'no'")
                continue
            if res == 'si':
                while True:
                    print("\nIngrese el número del área que desea ajustar o, ingrese el número 5 para salir")
                    try:
                        zona = int(input())
                    except ValueError:
                        print("Opción inválida. Por favor intenta de nuevo.")
                        continue

                    if zona == 5:
                        print("Has salido del control de temperaturas")
                        break
                    
                    if 1 <= zona <= 4:
                        temperatura = float(input(f"Ingresa la temperatura a la que desea ajustar el sensor {zona}, {sensores[zona-1]['nombre']}: "))
                        sensores[zona-1]['temperatura'] = temperatura
                        print(f"Temperatura del sensor {zona} ajustada a {temperatura}°C")
                    else:
                        print("Ingrese una opción válida")
                        
            else:
                print("\nPresiona Enter para volver al menú.")
                input()
                
        case 2: 
            while True:
                print("\nProgramación de horarios, elija el sensor que desee ajustar:")
                print("1. Sensor 1\n2. Sensor 2\n3. Sensor 3\n4. Sensor 4\n5. Salir")

                try:
                    menub = int(input())
                except ValueError:
                    print("Opción inválida. Por favor intenta de nuevo.")
                    continue

                if menub == 5:
                    print("Ha salido de la configuración de horarios")
                    break

                if 1 <= menub <= 4:
                    sensor = f'sensor{menub}'
                else:
                    print("Opción inválida. Por favor intenta de nuevo.")
                    continue

                while True:
                    print(f"Ingrese la hora en formato 24h (HH:MM) para iniciar la programación del sensor {sensor}")
                    hora_inicio = input()
                    if validate_time(hora_inicio):
                        break
                    print("Hora inválida. Por favor intente de nuevo.")

                temp_inicio = float(input(f"Ingrese la temperatura deseada para esta hora para el sensor {sensor}: "))

                while True:
                    print(f"Ingrese la hora en formato 24h (HH:MM) para finalizar la programación del sensor {sensor}:")
                    hora_fin = input()
                    if validate_time(hora_fin):
                        break
                    print("Hora inválida. Por favor intente de nuevo.")

                temp_fin = temperatura 

                horarios[sensor] = {
                    "hora_inicio": hora_inicio,
                    "hora_fin": hora_fin,
                    "temperaturai": temp_inicio,
                    "temperaturaf": temp_fin
                }

                print("\nPresiona Enter para volver al menú.")
                input()
                print("\n")

        case 3: 
            # Monitoreo de temperaturas
            print("\nMonitoreo de temperaturas en tiempo real:")
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(f"Hora actual: {current_time}")

            ambiente = 22  # Temperatura ambiente por defecto
            for sensor in sensores:
                sensor_num = f'sensor{sensor["numero"]}'
                if sensor_num in horarios:
                    horario = horarios[sensor_num]
                    hora_inicio = horario['hora_inicio']
                    hora_fin = horario['hora_fin']
                    temp_inicio = horario['temperaturai']
                    temp_fin = horario['temperaturaf']

                    # Convertimos las horas a formato de comparación
                    time_format = "%H:%M"
                    current_time_dt = datetime.datetime.strptime(current_time, time_format)
                    hora_inicio_dt = datetime.datetime.strptime(hora_inicio, time_format)
                    hora_fin_dt = datetime.datetime.strptime(hora_fin, time_format)

                    # Comprobamos si la hora actual está dentro del rango del horario
                    if hora_inicio_dt <= current_time_dt <= hora_fin_dt:
                        print(f"Área: {sensor['nombre']} (Número: {sensor['numero']}): Temperatura programada para esta hora es {temp_inicio}°C")
                    else:
                        print(f"Área: {sensor['nombre']} (Número: {sensor['numero']}): No hay temperatura programada, ajustando a temperatura ambiente {ambiente}°C")
                else:
                    print(f"Área: {sensor['nombre']} (Número: {sensor['numero']}): No tiene un horario programado.")

        case _:
            print("Ingrese una opción válida")
            print("\nPresiona Enter para volver.")
            input()
