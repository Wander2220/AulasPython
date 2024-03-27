num = int(input("Entre com um número: "))
counter=0
base = num
while base!=0:
 if num%base==0:
 counter = counter +1
 base = base -1
if counter == 2:
 print(f"O número {num} é primo!")
else:
 print(f"O número {num} não é primo!")