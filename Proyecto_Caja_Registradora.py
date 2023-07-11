print("Este programa le permitirá a los empleados de una tienda ordenar y etiquetar sus ítems, y a los usuarios conocer los productos en stock.")

print("Escriba a continuación el rol a desempeñar.")
print(''''
            (1)Comprador
            (2)Empleado
            (3)Salir del programa ''')
clase_usuario = str(input('----> '))
inventario = {'tomate': {'precio': 2.5, 'cantidad': 20}, 'cebolla': {'precio': 3.87, 'cantidad': 17}}
while isinstance(clase_usuario, str):
    if clase_usuario == "1":
        total = 0
        print('\nBienvenido, estos son los productos que tenemos a su disposición: ')
        print("Producto - Precio - Cantidad disponible")
        for producto in inventario:
            print([producto] + list(inventario[producto].values()))
        print('\nPor favor, indique la acción que desea realizar: ')
        print(''''
            (1)Procesar compra
            (2)Salir''')
        opcion_1 = input('----> ')
        if opcion_1 == '2':
            print("¡Estamos a su orden y gracias por preferirnos como su tienda de conveniencia favorita!")
            break
        elif opcion_1 == '1':
            continuar_compra = opcion_1.lower() in ["1"]
            while continuar_compra == True:
                producto = str(input('Indique el producto que desea añadir: '))                   
                cantidad = int(input('Indique la cantidad del producto añadido: '))
                if producto in inventario:
                    #procesas compra
                    if cantidad <= inventario[producto]['cantidad']: # validando cantidad
                        total += cantidad * inventario[producto]['precio']
                        print(f'El total de su compra hasta ahora es de: {total:.3f}')
                    else:
                        print('No hay suficiente cantidad en el local, lo sentimos.') 
                    # mensaje de stock insuficiente           
                else:
                    print('El producto indicado no se encuentra en el local, lo sentimos.')
                continuar_compras = input('¿Desea procesar otro producto? (sí/no): ')
                if continuar_compras.lower in ["si", "sí"]:
                    continuar_compra == True
                elif continuar_compras.lower() == 'no':
                    break
            print(f'El total final de su compra es de: {total}')  
        else:
            print("Ingrese una opción válida.")
            break
        print("¡Estamos a su orden y gracias por preferirnos como su tienda de conveniencia favorita!")
        break
        #else:
            #print('opcion no valida') 
    elif clase_usuario == "2":
        print('\nBienvenido, estos son los productos en inventario: ')
        for producto in inventario:
            print([producto] + list(inventario[producto].values()))        
        agregar_producto = input("¿Desea agregar un producto al inventario? (sí/no): ")
        if  agregar_producto.lower() not in ["si", "sí", "no"]:
            print("Ha ingresado una respuesta inadecuada.")
            break
        else:
            continuar = agregar_producto.lower() in ["si", "sí"]
            while continuar == True:
                producto = str(input("Ingrese el producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad en stock del producto: "))
                inventario.update({producto: {"precio": precio, "cantidad": cantidad}})
                agregar_producto = input("¿Desea agregar otro producto a inventario? (sí/no): ")
                if agregar_producto.lower() in ["no"]:
                    break
                elif agregar_producto.lower() not in ["si", "sí", "no"]:
                    print('''
                        Ha ingresado un valor inadecuado. Se culminará el proceso.''')
                    break
        print("Los productos en stock son los siguientes: ")
        print("Producto - Precio - Cantidad disponible")
        for producto in inventario:
            print([producto] + list(inventario[producto].values()))
        print('\nPor favor, indique la acción que desea realizar: ')
        print(''''
            (0)Salir
            (1)Cambiar al menú de usuario''')    
        clase_usuario = input('----> ')
        if clase_usuario == "0":
            break
        else:
            print("Por favor, ingrese '0' o '1'")
    elif clase_usuario == "3":
        print("¡Estamos a su orden y gracias por preferirnos como su tienda de conveniencia favorita!")
        break
    else:
        print("Debe identificarse como comprador o empleado según las opciones a continuación:")
        print(''''
            (1)Comprador
            (2)Empleado
            (3)Salir del programa  ''')
        clase_usuario = str(input('----> '))
        if clase_usuario == "3":
            break