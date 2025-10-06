import os
os.system("cls")


num = []

for i in range(5):
    nm = int(input("Digite um número: "))
    num.append(nm)

num.sort()

print("Números em ordem crescente:")
for i in num:
    print(i)