# Segunda questão da ficha de exercícios 02
import os
os.system("cls")

nomes =[]
idades = []

qtd = int(input("Digite a quantidade de funcionários aptos para a aposentadoria: "))

for i in range(qtd):
    while True:
        nome = input(f"Digite o nome do funcionário {len(nomes)+1}: ")
        idade = int(input(f"Digite a idade do funcionário {len(nomes)+1}: "))
        if idade >= 60:
            nomes.append(nome)
            idades.append(idade)
            break
        else:
            print(f"O funcionário {nome} não pode se aposentar ainda. Insira um funcionário com idade válida.")

print("\nFuncionários a se aposentar em 2025: ")
for nome, idade in zip(nomes, idades):
    print(f"Nome: {nome} ---- Idade: {idade} anos")

if nomes:
    id_mais_antigo = idades.index(max(idades))
    print(f"\nFuncionário mais antigo: {nomes[id_mais_antigo]} ")
    media_idade = sum(idades) / len(idades)
    print(f"\nMédia de idade dos funcionários: {media_idade:.2f} anos")



