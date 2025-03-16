def fibonacci(n, fib_list=[0, 1]):

    if n < len(fib_list):
        return fib_list[n]
    
    next_fib = fibonacci(n - 1, fib_list) + fibonacci(n - 2, fib_list)
    
    fib_list.append(next_fib)
    
    return next_fib

n = int(input("Ingrese el numero entero: ")) 
print(f"El término {n} de Fibonacci es: {fibonacci(n)}")

