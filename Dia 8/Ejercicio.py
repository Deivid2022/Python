import json
from operator import itemgetter

def cargar_json(Archivo_json):
  with open(Archivo_json, 'r') as Archivo:
    data = json.load(Archivo)
  return data 

def guardar_json(datos):
  with open(Archivo_json, 'w') as Archivo:
    Archivo.write(datos)

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

def clientes(Archivo_json):
  data = cargar_json(Archivo_json)
  clientes = data['ventas']['clientes']
  for i in clientes:
    print(i)

def comerciales(Archivo_json):
  data = cargar_json(Archivo_json)
  comerciales = data['ventas']['comerciales']
  for i in comerciales:
    print(i)

def pedidos(Archivo_json):
  data = cargar_json(Archivo_json)
  pedidos = data['ventas']['pedidos']
  for i in pedidos :
    print(i)
    
def modificar_clientes(Archivo_json, id_json):
  data = cargar_json(Archivo_json)
  clientes = data['ventas']['clientes']
  print('Datos actuales:')
  for i in clientes:
    print(i)
  for cliente in clientes:
    if cliente['id'] == id_json:
      id = int(input('Ingresa el nuevo id: '))
      nombre = input('Ingresa el nuevo nombre: ')
      apellido1 = input('Ingesa el nuevo apellido1: ')
      apellido2 = input('Ingresa el nuevo apellido2: ')
      ciudad = input('Ingresa la nueva ciudad: ')
      categoria = int(input('Ingresa la nueva categoria: '))
      clientes['id'] = id
      clientes['nombre'] = nombre
      clientes['apellido1'] = apellido1
      clientes['apellido2'] = apellido2
      clientes['ciudad'] = ciudad
      clientes['categoria'] = categoria
  
  guardar_json(clientes)
  
def menu2():
  print('1. Ejecutar')
  print('2. Modificar')
  

def menu():
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
  print('11. Devuelve un listado de los clientes')
  print('12. Devuelve un listado de los comerciales')
  print('13. Devuelve un listado de los pedidos')

Archivo_json = 'data.json'
while True:
  menu2()
  num1 = input('Ingrese la posicion de lo que deseas hacer ')
  if num1 == '1':
    menu()
    num = input('Escribe la posición de lo que quieras ver ')
  
<<<<<<< HEAD
  menu()
  num = input('Escribe la posición de lo que quieras ver(escribe salir si lo deseas) ')
  
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
  elif num == 'salir':
    print('Hasta luego')
    break
  else:
    print('Esta posicion no se encuentra')
=======
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
    elif num == '11':
      clientes(Archivo_json)
    elif num == '12':
      comerciales(Archivo_json)
    elif num == '13':
      pedidos(Archivo_json)
    else:
      print('Esta posicion no se encuentra')
  elif num1 == '2':
    ccp = input('ingresa la posición del que quieras modificar ')
    if ccp == '1':
      modificar_clientes(Archivo_json)
      
  
>>>>>>> dffe93a539ecfe4e4985a5a05e6909f455c6be67
    
  