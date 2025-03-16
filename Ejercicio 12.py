from cifrador_cesar import CifradorCesar

desplazamiento = 3
cifrador = CifradorCesar(desplazamiento)

mensaje_original = "Hola, mundo!"
print("Mensaje original:", mensaje_original)

mensaje_cifrado = cifrador.cifrar(mensaje_original)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = cifrador.descifrar(mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)
