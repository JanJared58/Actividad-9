def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convertir_fahrenheit_a_celsius(fahrenheit):

    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\nMenú de Conversión de Temperaturas:")
        print("1. Convertir Celsius a Fahrenheit")
        print("2. Convertir Fahrenheit a Celsius")
        print("3. Salir")
        
        opcion = input("Elige una opción (1/2/3): ")
        
        if opcion == "1":
        
            celsius = float(input("Introduce la temperatura en grados Celsius: "))
            fahrenheit = convertir_celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
        elif opcion == "2":
            
            fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
            celsius = convertir_fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}°F equivalen a {celsius:.2f}°C")
        elif opcion == "3":
            print("¡Adios!")
            break
        else:
            print("Opción inválida. Elige una opción válida.")

if __name__ == "__main__":
    main()
