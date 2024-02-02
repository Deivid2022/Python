def proceso(productos):
    producto = str (input("Escribe el producto que desees llevar: ")).lower()
    if producto in productos["Productos"] :
        cantidad = int (input("Ingrese la cantidad que desea de este producto: "))
        IndiceProducto = productos["Productos"].index(producto)
        precioTotal = productos["valor"][IndiceProducto]
        precioTotal = precioTotal * cantidad
        print(f"Tu compra tiene un total de $",precioTotal,)
    else:
        print("El producto no se encuentra disponible en la tienda.")