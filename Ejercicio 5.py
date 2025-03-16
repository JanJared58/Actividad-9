def suma_numeros_naturales(n):

    if n == 0:
        return 0 
    else:
        return n + suma_numeros_naturales(n - 1)  

n = int(input("Ingrese el numero: "))  
resultado = suma_numeros_naturales(n)
print(f"La suma de los primeros {n} números naturales es {resultado}")
