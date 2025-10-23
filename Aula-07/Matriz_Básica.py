matriz = []

for i in range(3):
  linha = []
  for j in range(3):
    valor = int(input(f"Qual o valor para a posição [{i+1};{j+1}]: "))
    linha.append(valor)
  matriz.append(linha)

for linha in matriz:
  print(linha)