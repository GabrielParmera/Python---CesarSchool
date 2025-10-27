def verificar_impeachment(total_jogadores, votos):
  votos_favoraveis = 0
  for voto in votos:
    if voto == 1:
      votos_favoraveis += 1

  if votos_favoraveis >= (2/3) * total_jogadores:
    return "impeachment"
  else:
    return "acusacao arquivada"

total_jogadores = int(input())
votos_str = input()
votos = list(map(int, votos_str.split()))

resultado = verificar_impeachment(total_jogadores, votos)
print(f"{resultado}")