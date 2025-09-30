# Quarta questão da ficha de exercício 02
import os
os.system("cls")

matriz = []
print("Digite os valores inteiros para a matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Linha {i}, Coluna {j}: "))
        linha.append(valor)
    matriz.append(linha)

coluna = int(input("\nDigite o número da coluna (0, 1 ou 2): "))
operacao = input("Digite a operação ([S]oma ou [P]roduto): ").strip().upper()

print("\nMatriz:")
for linha in matriz:
    print("\t".join(str(x) for x in linha))

if operacao == 'S':
    resultado = sum(matriz[i][coluna] for i in range(3))
    print(f"\nSoma dos elementos da coluna {coluna}: {resultado}")
elif operacao == 'P':
    produto = 1
    for i in range(3):
        produto *= matriz[i][coluna]
    print(f"\nProduto dos elementos da coluna {coluna}: {produto}")
else:
    print("Operação inválida. Use 'S' para soma ou 'P' para produto.")
