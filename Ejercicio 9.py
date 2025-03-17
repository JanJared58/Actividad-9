from calculadora_cientifica import CalculadoraCientifica

def main():

    calculadora = CalculadoraCientifica()

    print("=== Calculadora Científica ===")
    
    numero = 16
    print(f"Raíz cuadrada de {numero}: {calculadora.calcular_raiz_cuadrada(numero)}")

    base, exponente = 2, 8
    print(f"{base} elevado a la {exponente}: {calculadora.calcular_potencia(base, exponente)}")

    angulo = 45
    print(f"Seno de {angulo}°: {calculadora.calcular_seno(angulo)}")
    print(f"Coseno de {angulo}°: {calculadora.calcular_coseno(angulo)}")
    print(f"Tangente de {angulo}°: {calculadora.calcular_tangente(angulo)}")

    log_numero, log_base = 100, 10
    print(f"Logaritmo base {log_base} de {log_numero}: {calculadora.calcular_logaritmo(log_numero, log_base)}")

if __name__ == "__main__":
    main()
