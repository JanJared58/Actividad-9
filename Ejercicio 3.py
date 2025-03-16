def contar_vocales_usuario():
   
    cadena = input("Introduce una cadena de texto: ")
    
    vocales = "aeiou"
   
    cadena = cadena.lower()
 
    resultado = [(vocal, cadena.count(vocal)) for vocal in vocales]
    return resultado

if __name__ == "__main__":
    resultado = contar_vocales_usuario()
    print("Vocales y sus apariciones:", resultado)

