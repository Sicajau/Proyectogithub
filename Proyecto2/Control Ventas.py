#Proyecto Numero 2
#1990-18-10113
#Erick Estuardo Sicajau Turuy
#Seccion C

import json
import os
os.system('cls')
basedatos=[]
print("\t\t\tMENU \n\t1)-Registro Cliente Estandar\n\t2)-Registro Cliente Miembro\n\t3)-Mostrar Clientes Registrados")

opcion=int(input("Elige un Opcion: "))
os.system("cls")
if opcion == 1:
    opcion2=int(input("\n\tDigite un opcion\n\t1)-Motocicleta(Q.15)\n\t2)-Automovil(Q.30)\n\t3)-Camioneta(Q.50)\n\t"))
    os.system("cls")
    print("\t\t\tRegistro Clientes Estandar\n")
    if opcion2==1:
        motocicleta = {}
        tipo = input("Ingrese tipo de Vehiculo: ")
        precio = int(input("Ingrese el precio: "))
        cliente = input("Ingrese nombre: ")
        finsemana=input("Es fin de semana: ").lower()
        if finsemana == 'si':
            descuento = precio * 0.10
            descuentototal = precio - descuento
            precio = descuentototal
        else:
            print("\nNo tiene descuento de fin de semana\n")

        motocicleta['tipo']=tipo
        motocicleta['cliente']=cliente
        motocicleta['precio']=precio
        motocicleta['finsemana']=finsemana

        basedatos.append(motocicleta)
        with open('basedatos.json','w') as archivo:
            json.dump(basedatos,archivo)
            print(basedatos)

    elif opcion2==2:
        automovil = {}
        tipo = input("Ingrese tipo de Vehiculo: ")
        precio = int(input("Ingrese el precio: "))
        cliente = input("Ingrese nombre: ")
        finsemana = input("Es fin de semana: ").lower()
        if finsemana == 'si':
            descuento = precio * 0.10
            descuentototal = precio - descuento
            precio = descuentototal
        else:
            print("\nNo tiene descuento de fin de semana\n")
        automovil["tipo"] = tipo
        automovil["cliente"] = cliente
        automovil['precio']=precio
        automovil["finsemana"] = finsemana

        basedatos.append(automovil)
        with open('basedato.json','w') as archivo:
            json.dump(basedatos,archivo)
            print(basedatos)

    elif opcion2==3:
        camioneta={}
        tipo=input("ingrese tipo de vehiculo: ")
        precio=int(input("Ingrese el precio: "))
        cliente=input("Ingrese Cliente: ")
        finsemana = input("Es fin de semana: ").lower()
        if finsemana == 'si':
            descuento = precio * 0.10
            descuentototal = precio - descuento
            precio = descuentototal
        else:
            print("\nNo tiene descuento de fin de semana\n")
        camioneta["tipo"]=tipo
        camioneta['cliente']=cliente
        camioneta["precio"]=precio
        camioneta["finsemana"]=finsemana
        basedatos.append(camioneta)
        with open('basedatos.json','w') as archivo:
            json.dump(basedatos,archivo)
            print(basedatos)
    else:
        print("Opcion incorecta inicia nuevamente")
    os.system('cls')
elif opcion==2:
    opcion2 = int(input("\n\tDigite un opcion\n\t1)-Motocicleta(Q.15)\n\t2)-Automovil(Q.30)\n\t3)-Camioneta(Q.50)\n\t"))
    os.system('cls')
    print("\t\tRegistrar Cliente Miembro\n")

    if opcion2 == 1:
        motocicleta = {}
        tipo = input("Ingrese tipo de Vehiculo: ")
        precio = int(input("Ingrese el precio: "))
        miembro=precio*0.10
        miembrodes=precio-miembro
        precio=miembrodes
        cliente = input("Ingrese nombre: ")
        finsemana = input("Es fin de semana: ").lower()
        if finsemana == 'si':
            descuento = precio * 0.10
            descuentototal = precio - descuento
            precio = descuentototal
        else:
            print("\nNo tiene descuento de fin de semana\n")
        motocicleta['tipo'] = tipo
        motocicleta['cliente'] = cliente
        motocicleta['precio']=precio
        motocicleta['finsemana'] = finsemana

        basedatos.append(motocicleta)
        with open('basedatos.json','w') as archivo:
            json.dump(basedatos,archivo)
            print(basedatos)

    elif opcion2 == 2:
        automovil = {}
        tipo = input("Ingrese tipo de Vehiculo: ")
        precio = int(input("Ingrese el precio: "))
        miembro=precio*0.10
        miembrodes=precio-miembro
        precio=miembrodes
        cliente = input("Ingrese nombre: ")
        finsemana = input("Es fin de semana: ").lower()
        if finsemana == 'si':
            descuento = precio * 0.10
            descuentototal = precio - descuento
            precio = descuentototal
        else:
            print("\nNo tiene descuento de fin de semana\n")
        automovil["tipo"] = tipo
        automovil["cliente"] = cliente
        automovil['precio']=precio
        automovil["finsemana"] = finsemana

        basedatos.append(automovil)
        with open('basedatos.json','w') as archivo:
            json.dump(basedatos,archivo)
            print(basedatos)

    elif opcion2 == 3:
        camioneta = {}
        tipo = input("ingrese tipo de vehiculo: ")
        precio = int(input("Ingrese el precio: "))
        miembro=precio*0.10
        miembrodes=precio-miembro
        precio=miembrodes
        cliente = input("Ingrese Cliente: ")
        finsemana = input("Es fin de semana: ").lower()
        if finsemana == 'si':
            descuento = precio * 0.10
            descuentototal = precio-descuento
            precio = descuentototal
        else:
           print("\nNo tiene descuento de fin de semana\n")
        camioneta["tipo"] = tipo
        camioneta['cliente']=cliente
        camioneta["precio"] = precio
        camioneta["finsemana"] = finsemana
        basedatos.append(camioneta)
        with open('basedatos.json','w') as archivo:
            json.dump(basedatos,archivo)
            print(basedatos)


    else:
        print("Opcion incorecta inicia nuevamente")
elif opcion==3:
    os.system('cls')
    print("\n\tVisualizacion de base de datos\n")
    with open('basedatos.json') as archivo:
        visual=json.load(archivo)
    print(visual)
    
else:
    print("ingresa una opcion valida")