import os
os.system("cls")
# ATIVIDADE 2
distancia = float(input("Digite a distância: "))
velocidade = float(input("Digite a velocidade: "))
combustivel = float(input("Digite o consumo médio de combustível: "))
preco = float(input("Digite o preço do combustível: "))

tempo = distancia/velocidade
qtd_total = distancia/combustivel
total = qtd_total * preco

print(f"A duração da viagem foi de {tempo:.2f} horas com o gasto de combustível de {qtd_total:.2f} litros, sendo o custo total de {total:.2f} reais.")

