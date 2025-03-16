def promedio(*lista):

    prom = sum(lista)/len(lista)
    return prom

numeros = input("Introduce los números separados por espacios: ")

numeros_lista = []
for numero in numeros.split():
    numeros_lista.append(int(numero))


print(f"El promedio de los números es: {promedio(*numeros_lista)}")
