matriz = []
somaim = 0
somacoluna = 0

for i in range(3):
  linha = []
  for j in range(3):
    valor = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
    linha.append(valor)
  matriz.append(linha)

print("\nMatriz 3x3")
for linha in matriz:
  print(linha)

#Soma dos ímpares
for i in matriz:
  for j in i:
    if j % 2 != 0:
      somaim += j
print(f"\nA soma dos números ímpares é: {somaim}")

#Soma da primeira coluna
for i in matriz:
  somacoluna += i[0]

print(f"\nA soma dos valores da primeira coluna é: {somacoluna}")

#Menor da terceira coluna
terceira = matriz[2]
menor = min(terceira)
print(f"\nO menor valor da terceira coluna é: {menor}")