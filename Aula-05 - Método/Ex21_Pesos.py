import os
os.system("cls")

pesos = []

qtd = int(input("Digite a quantidade de produtos vendidos: "))

for i in range (qtd):
  peso = float(input("Digite o peso do produto: "))
  pesos.append(peso)

soma = sum(pesos)

print(f"O peso médio é: {sum(pesos)/qtd:.2f}")
print(f"O maior peso é: {max(pesos)}")
print(f"O menor peso é: {min(pesos)}")
print(f"Ao todo serão arrecadados: {soma*4.35} reais ")