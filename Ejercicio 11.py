from conversor_unidades import ConversorUnidades

def main():
    conversor = ConversorUnidades()

    print("=== Conversor de Unidades ===")
    
    metros = 10
    print(f"{metros} metros equivalen a {conversor.metros_a_pies(metros):.2f} pies")
    
    kilogramos = 5
    print(f"{kilogramos} kilogramos equivalen a {conversor.kilogramos_a_libras(kilogramos):.2f} libras")
    
    celsius = 25
    print(f"{celsius}°C equivalen a {conversor.celsius_a_fahrenheit(celsius):.2f}°F")
    
    litros = 3
    print(f"{litros} litros equivalen a {conversor.litros_a_galones(litros):.2f} galones")
    
    metros_cuadrados = 20
    print(f"{metros_cuadrados} metros cuadrados equivalen a {conversor.metros_cuadrados_a_pies_cuadrados(metros_cuadrados):.2f} pies cuadrados")
    
    kilometros = 15
    print(f"{kilometros} kilómetros equivalen a {conversor.kilometros_a_millas(kilometros):.2f} millas")

if __name__ == "__main__":
    main()
