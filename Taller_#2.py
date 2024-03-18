## Este programa permite controlar el inventario de una tienda
## Para esto se pone a disposición un menú con 6 opciones con las que se puede controlar el inventario



import random
import os

class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre, cantidad, umbral):
        if nombre in self.inventario:
            print("¡Alerta! Producto ya existe. Utilice la opción 6 para modificar.")
        else:
            self.inventario[nombre] = [cantidad, umbral]
            print("Producto agregado con éxito.")

        input("\nPresione enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")    

    def simular_consumo(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\nSimulación de consumo:")
        alertas = []
        for producto, datos in self.inventario.items():
            cantidad_actual, umbral = datos
            if cantidad_actual > 0:
                consumo = random.randint(1, cantidad_actual)
                datos[0] -= consumo
                print(f"Consumo de {producto}: {consumo}")
                if datos[0] < datos[1]:
                    alertas.append(producto)
            else:
                print(f"No se puede realizar consumo de {producto} ya que la cantidad actual es 0.")
        if alertas:
            print("\n¡Alerta! Es necesario reordenar los siguientes productos:")
            for producto in alertas:
                cantidad_actual, umbral = self.inventario[producto]
                print(f"{producto}: Cantidad actual: {cantidad_actual}, Umbral mínimo: {umbral}")
        
        input("\nPresione enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_reporte(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\033[93mReporte de inventario:\033[0m")
        print("\033[93m{:<20} {:<10} {:<10}\033[0m".format("Producto", "Cantidad", "Umbral"))
        print("-" * 40)
    
        for producto, datos in self.inventario.items():
            cantidad, umbral = datos
            if cantidad < umbral:
                print(f"\033[91m{producto:<20} {cantidad:<10} {umbral:<10}\033[0m")
            else:
                print(f"{producto:<20} {cantidad:<10} {umbral:<10}") 
        input("\nPresione enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")

    def calcular_inventario_total(self):
        os.system("cls" if os.name == "nt" else "clear")
        total = sum(cantidad for cantidad, _ in self.inventario.values())
        print("\nInventario total:", total)
        input("\nPresione enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")

    def verificar_alertas_reorden(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\nAlertas de reorden:")
        for producto, datos in self.inventario.items():
            cantidad, umbral = datos
            if cantidad < umbral:
                print(f"Alerta: Es necesario reordenar {producto}. Cantidad actual: {cantidad}, Umbral mínimo: {umbral}")
            else:
                print('No hay aletas')     
        input("\nPresione enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")

    def reabastecer_producto(self, nombre, cantidad):
        os.system("cls" if os.name == "nt" else "clear")
        while nombre not in self.inventario:
            print("El producto ingresado no existe en el inventario.")
            respuesta = input("¿Desea intentarlo de nuevo (s/n)?: ").lower()
            if respuesta != 's':
                return
            nombre = input("Ingrese el nombre del producto a reabastecer: ")
        self.inventario[nombre][0] += cantidad
        print(f"Producto {nombre} reabastecido exitosamente.")
        input("\nPresione enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")

def main():
    inventario = Inventario()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nMenú de gestión de inventario")
        print("1. Agregar producto")
        print("2. Simular consumo")
        print("3. Mostrar reporte de inventario")
        print("4. Calcular inventario total")
        print("5. Verificar alertas de reorden")
        print("6. Reabastecer producto")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = obtener_entero("Ingrese la cantidad existente: ")
            umbral = obtener_entero("Ingrese el umbral mínimo: ")
            inventario.agregar_producto(nombre, cantidad, umbral)
        elif opcion == "2":
            inventario.simular_consumo()
        elif opcion == "3":
            inventario.mostrar_reporte()
        elif opcion == "4":
            inventario.calcular_inventario_total()
        elif opcion == "5":
            inventario.verificar_alertas_reorden()
        elif opcion == "6":
            nombre = input("Ingrese el nombre del producto a reabastecer: ")
            cantidad = obtener_entero("Ingrese la cantidad a agregar: ")
            inventario.reabastecer_producto(nombre, cantidad)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
        
        os.system("cls" if os.name == "nt" else "clear")

def obtener_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero.")

if __name__ == "__main__":
    main()
