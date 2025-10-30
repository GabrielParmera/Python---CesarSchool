matriz = [[], [], []]
media = 0
soma = 0
produto_diagonal = 1
valores_menores = []

for i in range(3):
  for j in range(3):
    valor = int(input(f"Qual o valor na posição[ {i} ][ {j} ]: "))
    matriz[i].append(valor)
    soma += matriz[i][j]
    if i == j:
      produto_diagonal *= matriz[i][j]

#print da matriz
for i in range(3):
  for j in range(3):
    print(f"[{matriz[i][j]}]", end=' ')
  print()

media = soma / 9

print(f"\nO produto dos elementos da diagonal é: {produto_diagonal}")
print(f"A média dos elementos da matriz é: {media}")

maior_segunda_coluna = matriz[0][1]
for i in range(1, 3):
  if matriz[i][1] > maior_segunda_coluna:
    maior_segunda_coluna = matriz[i][1]

print(f"O maior número da segunda coluna é: {maior_segunda_coluna}")

for i in range(3):
  for j in range(3):
    if matriz[i][j] < media:
      valores_menores.append(matriz[i][j])

print(f"Os valores menores que a média são: {valores_menores}")