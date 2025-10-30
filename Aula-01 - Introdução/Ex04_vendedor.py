import os
os.system("cls")

qtd_carros = int(input("Digite a qtd de carros vendidos: "))
comissao = float(input("Digite a comissão: "))
salario = float(input("Digite o salário: "))

bonus = salario + comissao + (0.05 * qtd_carros)


print(f"O vendedor vendeu {qtd_carros} com o salario {salario:.2f} e comissão {comissao}, além do bônus {bonus}.")
