import os
os.system("cls")
from datetime import date

menor_idade = 0
maior_idade = 0
ano_atual = date.today().year

for i in range(5):
    ano_nascimento = int(input(f"Digite o ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    if idade < 18:
        menor_idade += 1
    else:
        maior_idade += 1

print(f"Total de pessoas menores de idade: {menor_idade}")
print(f"Total de pessoas maiores de idade: {maior_idade}")