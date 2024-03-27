def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Entre com um número n: "))
count = 0
num = 2

print(f"Os primeiros {n} números primos são:")

while count < n:
    if is_prime(num):
        print(num)
        count += 1
    num += 1
