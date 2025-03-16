from vector_3d import Vector3D

def main():

    vector1 = Vector3D(3, 4, 5)
    vector2 = Vector3D(1, 2, 3)

    print("=== Operaciones con Vectores 3D ===")
    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")

    suma = vector1.suma(vector2)
    print(f"Suma: {suma}")

    resta = vector1.resta(vector2)
    print(f"Resta: {resta}")

    producto_escalar = vector1.producto_escalar(vector2)
    print(f"Producto escalar: {producto_escalar}")

    modulo_vector1 = vector1.modulo()
    print(f"Módulo de Vector 1: {modulo_vector1:.2f}")

    modulo_vector2 = vector2.modulo()
    print(f"Módulo de Vector 2: {modulo_vector2:.2f}")

    try:
        normalizado_vector1 = vector1.normalizar()
        print(f"Vector 1 normalizado: {normalizado_vector1}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
