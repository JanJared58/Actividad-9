def ordenar_lista_usuario():
   
    entrada = input("Introduce las palabras separadas por comas: ")
    
    lista_palabras = [palabra.strip() for palabra in entrada.split(",")]
    
    return sorted(lista_palabras)

if __name__ == "__main__":
    lista_ordenada = ordenar_lista_usuario()
    print("Lista ordenada:", lista_ordenada)
