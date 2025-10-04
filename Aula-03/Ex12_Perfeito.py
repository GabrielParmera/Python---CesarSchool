import os
os.system("cls")

num = int(input("Digite um número: "))

soma = 0

for i in range(1, num):   #i é os divisores
    if num % i == 0:
        soma += i

if num == soma:
    print(f"O número {num} é perfeito.")
else:
    print(f"O número {num} não é perfeito.")