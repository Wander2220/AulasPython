def separar_digitos(num):
    num_str = str(num)
    for digito in num_str:
        print(digito, end="   ")

try:
    
    num = int(input("Digite um número de cinco dígitos:  "))
    
    print("Os dígitos separados por três espaços são:   ")
    separar_digitos(num)
    
except ValueError:
    print("Ocorreu um erro")