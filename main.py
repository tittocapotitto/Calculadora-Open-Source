from sumar import sumar
from resta import restar
from multplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    """
    Muestra el menú de opciones de la calculadora.
    """
    print("\n--- Calculadora ---")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Sumar N números")
    print("6. Salir")

def main():
    """
    Función principal de la calculadora.
    """
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                print(f"Resultado: {sumar(num1, num2)}")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa números.")

        elif opcion == '2':
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                print(f"Resultado: {restar(num1, num2)}")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa números.")
        
        elif opcion == '3':
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                print(f"Resultado: {multiplicar(num1, num2)}")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa números.")

        elif opcion == '4':
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                print(f"Resultado: {dividir(num1, num2)}")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa números.")

        elif opcion == '5':
            try:
                numeros_str = input("Ingresa los números a sumar, separados por comas (ej. 1,2,3): ")
                numeros = [float(n.strip()) for n in numeros_str.split(',')]
                print(f"Resultado: {suma_avanzada(*numeros)}")
            except ValueError:
                print("Entrada no válida. Asegúrate de ingresar números separados por comas.")

        elif opcion == '6':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()
