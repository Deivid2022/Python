import json
from operator import itemgetter

def cargar_json(Archivo_json):
  with open(Archivo_json, 'r') as Archivo:
    data = json.load(Archivo)
  return data 

def fechas_recientes(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  pedidos_ordenados = sorted(pedidos, key=lambda x: x["fecha"], reverse=True)
  for i in pedidos_ordenados:
     print(i)

def Mayor_Valor(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  pedidos_ordenados_por_valor = sorted(pedidos, key=lambda x: x['total'], reverse=True)
  dos_pedidos_mas_valorados = pedidos_ordenados_por_valor[:2]
  for i in dos_pedidos_mas_valorados:
    print(i)

def indentificadores_clientes(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  clientes_pedidos = set()
  for pedido in pedidos:
    clientes_pedidos.add(pedido['id_cliente'])
  return list(clientes_pedidos)

def pedidos_2017_mayor_500(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  pedidos_2017_mayor_500 = [pedido for pedido in pedidos if pedido['fecha'].startswith('2017') and pedido['total'] > 500]
  for i in pedidos_2017_mayor_500:
    print(i)
    
def comerciales_comision(Archivo_json):
  data = cargar_json(Archivo_json)
  comerciales = data['ventas']['comerciales']
  comision_005_011 = [comercial for comercial in comerciales if 0.05 <= comercial['comision'] <= 0.11]
  for i in comision_005_011:
    print(i)

def comision_MayorValor(Archivo_json):
  data = cargar_json(Archivo_json)
  comerciales = data['ventas']['comerciales']
  comision = [comercial['comision'] for comercial in comerciales ]
  comision_alta = max(comision)
  return comision_alta

def clientes_sevilla(Archivo_json):
  data = cargar_json(Archivo_json)
  clientes = data['ventas']['clientes']
  ciudad_sevilla = [cliente for cliente in clientes if cliente['ciudad'] == 'Sevilla']
  ciudad_sevilla_ordenada = sorted(ciudad_sevilla, key = itemgetter('nombre','apellido1'))
  for i in ciudad_sevilla_ordenada:
    print(i)

def clientes_An(Archivo_json):
  data = cargar_json(Archivo_json)
  clientes = data['ventas']['clientes']
  clientes_filtrados = [cliente['nombre'] for cliente in clientes if cliente['nombre'].startswith('A') and cliente['nombre'].endswith('n')]
  clientes_filtrados += [cliente['nombre'] for cliente in clientes if cliente['nombre'].startswith('P')]
  clientes_filtrados_ordenados = sorted(clientes_filtrados)
  return clientes_filtrados_ordenados

def clientes_A(Archivo_json):
  data = cargar_json(Archivo_json)
  clientes = data['ventas']['clientes']
  clientes_A = [cliente['nombre'] for cliente in clientes if cliente['nombre'].startswith('A')]
  clientes_A_ordenados = sorted(clientes_A)
  return clientes_A_ordenados

def comerciales_Ruiz(Archivo_json):
  data = cargar_json(Archivo_json)
  comerciales = data['ventas']['comerciales']
  comerciales_ruiz = set()
  for comercial in comerciales:
    if 'Ruiz' in comercial.values():
      comerciales_ruiz.add(comercial['nombre'])
  return list(comerciales_ruiz)

def leer_clientes():
    with open('data.json') as archivo:
        datos = json.load(archivo)
        clientes = datos['ventas']['clientes']
        for i in clientes:
            print(i)

def añadir_clientes():
    with open('data.json', 'r') as archivo:
        datos = json.load(archivo)

    nuevo_cliente = {}
    nuevo_cliente['id'] = int(input('Ingrese el ID del nuevo cliente: '))
    nuevo_cliente['nombre'] = input('Ingrese el nombre del nuevo cliente: ')
    nuevo_cliente['apellido1'] = input('Ingrese el primer apellido del nuevo cliente: ')
    nuevo_cliente['apellido2'] = input('Ingrese el segundo apellido del nuevo cliente (opcional): ')
    nuevo_cliente['ciudad'] = input('Ingrese la ciudad del nuevo cliente: ')
    nuevo_cliente['categoria'] = int(input('Ingrese la categoría del nuevo cliente: '))

    datos["ventas"]["clientes"].append(nuevo_cliente)

    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo,indent=4) 

def actualizar_clientes():
    miVariable = open('data.json')
    datos = json.load(miVariable)
    clientes = datos['ventas']['clientes']
    id_json = int(input('Ingresa el id del cliente que quieras actualizar: '))
    for cliente in clientes:
        if cliente['id'] == id_json:
            nombre = input('Ingresa el nuevo nombre: ') 
            apellido1 = input('Ingresa el nuevo primer apellido: ')
            apellido2 = input('Ingresa el nuevo segundo apellido (opcional): ')
            ciudad = input('Ingresa la nueva ciudad: ')
            categoria = int(input('Ingrese la nueva categoria: ')) 
            cliente['nombre'] = nombre
            cliente['apellido1'] = apellido1
            cliente['apellido2'] = apellido2 
            cliente['ciudad'] = ciudad
            cliente['categoria'] = categoria
    
    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
        
def eliminar_clientes():
    miVariable = open('data.json')
    datos = json.load(miVariable)
    clientes = datos['ventas']['clientes']
    
    id_json = int(input('Ingresa el id del cliente que quieras eliminar: '))
    
    for cliente in clientes:
        if cliente['id'] == id_json:
            clientes.remove(cliente) 
            
    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def leer_comerciales():
    with open('data.json') as archivo:
        datos = json.load(archivo)
        comerciales = datos['ventas']['comerciales']
        for i in comerciales:
            print(i)


def añadir_comerciales():
    with open('data.json', 'r') as archivo:
        datos = json.load(archivo)

    nuevo_comercial = {}
    nuevo_comercial["id"] = int(input("Ingrese el ID del nuevo comercial: "))
    nuevo_comercial["nombre"] = input("Ingrese el nombre del nuevo comercial: ")
    nuevo_comercial["apellido1"] = input("Ingrese el primer apellido del nuevo comercial: ")
    nuevo_comercial["apellido2"] = input("Ingrese el segundo apellido del nuevo comercial: ")
    nuevo_comercial["comision"] = float(input("Ingrese la comision del nuevo comercial: "))

    datos["ventas"]["comerciales"].append(nuevo_comercial)

    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo,indent=4) 

def actualizar_comerciales():
    miVariable = open('data.json')
    datos = json.load(miVariable)
    comerciales = datos['ventas']['comerciales']
    id_json = int(input('Ingresa el id del comercial que quieras actualizar: '))
    for comercial in comerciales:
        if comercial['id'] == id_json:
            nombre = input('Ingresa el nuevo nombre: ') 
            apellido1 = input('Ingresa el nuevo primer apellido: ')
            apellido2 = input('Ingresa el nuevo segundo apellido: ')
            categoria = float(input('Ingrese la nueva comision: ')) 
            comercial['nombre'] = nombre
            comercial['apellido1'] = apellido1
            comercial['apellido2'] = apellido2 
            comercial['comision'] = categoria
    
    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def eliminar_comerciales():
    miVariable = open('data.json')
    datos = json.load(miVariable)
    comerciales = datos['ventas']['comerciales']
    
    id_json = int(input('Ingresa el id del comercial que quieras eliminar: '))
    
    for comercial in comerciales:
        if comercial['id'] == id_json:
            comerciales.remove(comercial) 
            
    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def leer_pedidos():
    with open('data.json') as archivo:
        datos = json.load(archivo)
        pedidos = datos['ventas']['pedidos']
        for i in pedidos:
            print(i)


def añadir_pedidos():
    with open('data.json', 'r') as archivo:
        datos = json.load(archivo)

    nuevo_pedido = {}
    nuevo_pedido["id"] = int(input("Ingrese el ID del nuevo pedido: "))
    nuevo_pedido["total"] = float(input("Ingrese el total del nuevo pedido: "))
    nuevo_pedido["fecha"] = input("Ingrese la fecha del nuevo pedido: ")
    nuevo_pedido["id_cliente"] = int(input("Ingrese el segundo apellido del nuevo cliente (opcional): "))
    nuevo_pedido["id_comercial"] = int(input("Ingrese la ciudad del nuevo cliente: "))

    datos["ventas"]["pedidos"].append(nuevo_pedido)

    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo,indent=4) 

def actualizar_pedidos():
    miVariable = open('data.json')
    datos = json.load(miVariable)
    pedidos = datos['ventas']['pedidos']
    id_json = int(input('Ingresa el id del pedido que quieras actualizar: '))
    for pedido in pedidos:
        if pedido['id'] == id_json:
            total = float(input('Ingresa el nuevo valor total: ') )
            fecha = input('Ingresa la nueva fecha: ')
            id_cliente = int(input('Ingresa el nuevo id_cliente: '))
            id_comercial = int(input('Ingrese el nuevo id_comercial: ')) 
            pedido['total'] = total
            pedido['fecha'] = fecha
            pedido['id_cliente'] = id_cliente
            pedido['id_comercial'] = id_comercial
    
    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)
        
def eliminar_pedidos():
    miVariable = open('data.json')
    datos = json.load(miVariable)
    pedidos = datos['ventas']['pedidos']
    
    id_json = int(input('Ingresa el id del pedido que quieras eliminar: '))
    
    for pedido in pedidos:
        if pedido['id'] == id_json:
            pedidos.remove(pedido) 
            
    with open('data.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def menu():
  print('1. Ejecutar')
  print('2. Modificar')

def menu1():
  print('1. Crear')
  print('2. Leer')
  print('3. Actualizar')
  print('4. Eliminar')

def menu2():
  print('1. Devuelve un listado con todos los pedidos que se han realizado')
  print('2. Devuelve todos los datos de los dos pedidos de mayor valor.')
  print('3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido')
  print('4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.')
  print('5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.')
  print('6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial.')
  print('7. Devuelve el identificador, nombre y primer apellido de aquellos clientes cuyo ciudad sea "Sevilla".')
  print('8. Devuelve un listado de los nombres de los clientes que empiezan por A y terminan por n y también los nombres que empiezan por P. ')
  print('9. Devuelve un listado de los nombres de los clientes que  empiezan por A.')
  print('10. Devuelve un listado con los nombres de los comerciales que tienen como apellido "Ruiz".')

Archivo_json = 'data.json'
while True:
  menu()
  decision = input('Ingresa que deseas hacer(posición)(escribe salir si lo deseas): ')
  if decision == '1':
    menu2()
    num = input('Escribe la posición de lo que quieras ver ')
        
    if num == '1': 
      fechas_recientes(Archivo_json)
    elif num == '2':
      Mayor_Valor(Archivo_json)
    elif num == '3': 
      print(indentificadores_clientes(Archivo_json))
    elif num == '4':
      pedidos_2017_mayor_500(Archivo_json)
    elif num == '5':
      comerciales_comision(Archivo_json)
    elif num == '6':
      print(comision_MayorValor(Archivo_json))
    elif num == '7':
      clientes_sevilla(Archivo_json)
    elif num == '8':
      print(clientes_An(Archivo_json))
    elif num == '9':
      print(clientes_A(Archivo_json))
    elif num == '10':
      print(comerciales_Ruiz(Archivo_json))
    else:
      print('Esta posicion no se encuentra')
  elif decision == '2':
    menu1()
    num1 = input('Escoge una: ')
    if num1 == '1':
      crear = input('Clientes - Comerciales - Pedidos: ').lower()
      if crear == 'clientes':
        añadir_clientes()
      elif crear == 'comerciales':
        añadir_comerciales()
      elif crear == 'pedidos':
        añadir_pedidos()
      else:
        print('Vuelve a escribirlo bien')
    elif num1 == '2':
      leer = input('Clientes - Comerciales - Pedidos: ').lower()
      if leer == 'clientes':
        leer_clientes()
      elif leer == 'comerciales':
        leer_comerciales()
      elif leer == 'pedidos':
        leer_pedidos()
      else:
        print('Vuelve a escribirlo bien')
    elif num1 == '3':
      actualizar = input('Clientes - Comerciales - Pedidos: ').lower()
      if actualizar == 'clientes':
        actualizar_clientes()
      elif actualizar == 'comerciales':
        actualizar_comerciales()
      elif actualizar == 'pedidos':
        actualizar_pedidos()
      else:
        print('Vuelve a escribirlo bien')
    elif num1 == '4':
      eliminar = input('Clientes - Comerciales - Pedidos: ').lower()
      if eliminar == 'clientes':
        eliminar_clientes()
      elif eliminar == 'comerciales':
        eliminar_comerciales()
      elif eliminar == 'pedidos':
        eliminar_pedidos()
      else:
        print('Vuelve a escribirlo bien')
  elif decision == 'salir':
    print('Hasta luego')
    break
  else:
    print('Vuelve a colocar una posición que se encuentre')