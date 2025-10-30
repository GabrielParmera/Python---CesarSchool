carros = 0
mais_novo = " "
mais_velho = " "
ano_novo = 0
ano_velho = 9999

while True:
    modelo = input("Digite o modelo do carro: ")
    ano = int(input("Digite o ano do carro: "))

    carros += 1


    if ano > ano_novo:
        ano_novo = ano
        mais_novo = modelo

    if ano < ano_velho:
        ano_velho = ano
        mais_velho = modelo

    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() == 'N':
        break

print(f"Total de carros cadastrados: {carros}")
print(f"Carro mais novo: {mais_novo} ({ano_novo})")
print(f"Carro mais velho: {mais_velho} ({ano_velho})")