# Terceira questão da ficha de exercício 02
import os
os.system("cls")

matriz = []

for i in range(3):
    linha = []
    print(f"Cadastro da profissão {i + 1}:")
    for j in range(3):
        if j == 0:
            valor = float(input("Digite o salário médio: R$ "))
        elif j == 1:
            valor = int(input("Digite o tempo mínimo de experiência (em anos): "))
        else:
            valor = float(input("Digite o valor da hora de trabalho: R$ "))
        linha.append(valor)
    matriz.append(linha)
    print()

print("\nMatriz de Profissões:")
for linha in matriz:
    print(linha)
media_salarial = sum(linha[0] for linha in matriz) / 3
soma_diagonal = sum(matriz[i][i] for i in range(3))

print(f"\nMédia salarial das três profissões: R$ {media_salarial:.2f}")
print(f"Soma dos valores da diagonal principal: {soma_diagonal:.2f}")
