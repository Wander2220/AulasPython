def fibonacci(n):
    if n <= 0:
        return "Por favor, forneça um número inteiro positivo maior ou igual a 1."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fib = [1, 1]  
        for i in range(2, n):
            next_term = fib[-1] + fib[-2]  
            fib.append(next_term)  
        return fib[-1] 

n = int(input("Digite o valor de n (n >= 3): "))
result = fibonacci(n)
print(f"O {n}-ésimo termo da série de Fibonacci é: {result}.")
