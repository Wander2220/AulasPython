def square_of_natural_number(n):
    if n == 1:
        return 1
    
    square = 1
    odd_number = 1
    
    for _ in range(2, n + 1):
        odd_number += 2
        square += odd_number
        
    return square

n = int(input("Digite um número natural: "))
result = square_of_natural_number(n)
print(f"O quadrado de {n} é {result}.")
