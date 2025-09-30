# Primeira questão da ficha de exercícios 02
import os
os.system("cls")

qtd = int(input("Digite a quantidade de mouses encontrados: "))

defeitos = [0, 0, 0, 0]

for i in range(qtd):
    tipo_defeito = int(input("Digite o tipo de defeito do mouse (1-4): "))
    if 1 <= tipo_defeito <= 4:
        defeitos[tipo_defeito - 1] += 1
    else:
        print("Tipo de defeito inválido.")

print("Relatório de Mouses:")
print(f"\nQuantidade total de mouses: {qtd}\n")
print("-"*75)
defeitos_titulos = [
    "1- Necessita da esfera",
    "2- Necessita de limpeza",
    "3- Necessita troca do cabo ou conector",
    "4- Quebrado ou inutilizado"
]
print(f"Título do Defeito\t\t\tQuantidade\t\tPercentual (%)")
for i in range(4):
    percentual = (defeitos[i]/qtd)*100 if qtd > 0 else 0
    print(f"{defeitos_titulos[i]:<35}\t\t{str(defeitos[i]):<10}\t\t{percentual:>8.2f}%")
