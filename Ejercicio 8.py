from temperatura import convertir_celsius_a_fahrenheit as c_to_f
from temperatura import convertir_fahrenheit_a_celsius as f_to_c

def main():
    while True:
        print("\nMenú de Conversión de Temperaturas:")
        print("1. Convertir Celsius a Fahrenheit")
        print("2. Convertir Fahrenheit a Celsius")
        print("3. Salir")
        
        opcion = input("Elige una opción (1/2/3): ")
        
        if opcion == "1":
            
            celsius = float(input("Introduce la temperatura en grados Celsius: "))
            fahrenheit = c_to_f(celsius)
            print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
        elif opcion == "2":
            # Fahrenheit a Celsius
            fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
            celsius = f_to_c(fahrenheit)
            print(f"{fahrenheit}°F equivalen a {celsius:.2f}°C")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
