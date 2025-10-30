import os
os.system("cls")

total = 0

while True:
    valor = float(input("Digite o valor do produto (ou 0 para finalizar): R$ "))

    if valor < 0:
        print("Valor Inválido.")
        continue
    elif valor == 0:
        break

    total += valor

if total > 1000:
    total *= 0.9

print(f"Total a pagar: R$ {total:.2f}")