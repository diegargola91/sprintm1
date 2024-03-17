import pandas as pd

# Clases

#La clase Producto representa cada producto con sus parámetros. Contiene funciones para obtener la información del producto y otra para modificar la información.
class Producto:
    def __init__(self, id, nombre, descripcion, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def obtener_info(self):
        return self.__dict__
    
    def modificar_info(self):
        print("Seleccione el campo a modificar\n")
        print("1. Id")
        print("2. Nombre")
        print("3. Descripcion")
        print("4. Cantidad")
        print("5. Precio\n")
        opcion = int(input("Opción: "))
        valor = input("Ingrese el nuevo valor: ")
        try:
            if opcion == 1:
                self.id = valor
            elif opcion == 2:
                self.nombre = valor
            elif opcion == 3:
                self.descripcion = valor
            elif opcion == 4:
                self.cantidad = valor
            elif opcion == 5:
                if type(valor) != str:
                    self.precio = float(valor)
                else:
                    print("Debe ingresar un número")
            else:
                print("Opción inválida")
        except ValueError:
            print("Opción inválida. Debe ingresar un número")

#La clase Inventario representa el arreglo de existencias que contiene todos los productos.
# Contiene funciones para buscar, listar, agregar, modificar o eliminar productos.
class Inventario(Producto):
    def __init__(self, existencias):
        self.existencias = existencias #Parámetro existencias contiene el arreglo de objetos Producto
        
    def agregar_producto(self):
        print("Ingrese los datos\n")
        id = input("Id: ")
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        guardar = input("Guardar cambios? s/n: ")
        if(guardar == "s"):
            Inventario_Arreglo.existencias.append(Producto(id, nombre, descripcion, cantidad, precio))
        print(Inventario_Arreglo.existencias)
    def buscar_por_id(self):
        producto = int(input("Buscar por id: "))
        existe = any(prod.id == producto for prod in self.existencias)
        if existe:
            return [obj for obj in self.existencias if obj.id == producto]
        else:
            print("No existe el producto con ese id.")
    def buscar_por_nombre(self):
        producto = input("Buscar producto por nombre: ")
        existe = any(prod.nombre.lower() == producto.lower() for prod in self.existencias)
        if existe:
            return [obj for obj in self.existencias if obj.nombre.lower() == producto.lower()]
        else:
                print("El/los producto(s) no se encuentra(n) en el inventario.")

    def eliminar_producto(self, producto):
            self.existencias.remove(producto)
    
    def modificar_producto(self, producto):
            producto.modificar_info()

    def mostrar_info(self, productos):
            for producto in productos:
                print(producto.obtener_info())

    def listar_productos(self):
        cantidad = len(self.existencias)
        monto = 0
        total_existencias = 0
        for existencia in self.existencias:
            monto = existencia.precio*existencia.cantidad + monto
            total_existencias = existencia.cantidad + total_existencias

        print("\nCantidad de productos: ",cantidad)
        print("Total existencias: ",total_existencias)
        print("Valor total de existencias: $",monto)
        print("Listado de productos")
        [print(existencia.__dict__) for existencia in self.existencias]


# Variables para el estado inicial del programa.
        
Productos = [ 
    Producto( 1, "Tomate", "Tomates de Limache", 20, 900),
    Producto( 2, "Lechuga", "Lechuga hidropónica", 15, 500)
]
Inventario_Arreglo = Inventario(Productos)

#Menu del programa para el usuario

while True:
    print("\nBienvenido al Control de Inventario\n")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Modificar Producto")
    print("4. Buscar Producto")
    print("5. Listar Productos")
    print("6. Salir\n")
    opcion = int(input("Seleccione una opción: "))

    if(opcion >= 1 and opcion <= 5):
        if(opcion == 1):
            Inventario_Arreglo.agregar_producto()
        elif opcion == 2:
            producto = Inventario_Arreglo.buscar_por_id()[0]
            Inventario_Arreglo.eliminar_producto(producto)
        elif opcion == 3:
            producto = Inventario_Arreglo.buscar_por_id()[0]
            Inventario_Arreglo.modificar_producto(producto)
        elif opcion == 4:
            buscar = int(input("Buscar por 1. Nombre o 2. Id ?: "))
            try:
                if buscar == 1: 
                    producto = Inventario_Arreglo.buscar_por_nombre()
                    Inventario_Arreglo.mostrar_info(producto)
                elif buscar == 2: 
                    producto = Inventario_Arreglo.buscar_por_id()
                    Inventario_Arreglo.mostrar_info(producto)
                else:
                    print("Ingrese una opción válida.")
            except ValueError: 
                print("Debe ingresar un número válido de opción.")
        else:
            Inventario_Arreglo.listar_productos()
    elif opcion == 6:
        break
    else:
        print("Ingrese una opción válida")
