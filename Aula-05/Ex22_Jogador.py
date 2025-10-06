votos = []
jog7 = []
jog8 = []
jog9 = []
jog10 = []
jog11 = []

while (True):
  voto = int(input("Digite o voto para melhor jogador: "))
  votos.append(voto)
  if voto == 0:
    break
  elif voto == 7:
    jog7.append(voto)
  elif voto == 8:
    jog8.append(voto)
  elif voto == 9:
    jog9.append(voto)
  elif voto == 10:
    jog10.append(voto)
  elif voto == 11:
    jog11.append(voto)
  else:
    print("Voto Inválido")
    continue

print(f"Total de votos: {len(votos)}\n")
print(f"Total de votos para o jogador 7: {len(jog7)}\n")
print(f"Total de votos para o jogador 8: {len(jog8)}\n")
print(f"Total de votos para o jogador 9: {len(jog9)}\n")
print(f"Total de votos para o jogador 10: {len(jog10)}\n")
print(f"Total de votos para o jogador 11: {len(jog11)}\n")

print(f"O percentual de votos para o jogador 7 é: {len(jog7)}/{len(votos)}\n")
print(f"O percentual de votos para o jogador 8 é: {len(jog8)}/{len(votos)}\n")
print(f"O percentual de votos para o jogador 9 é: {len(jog9)}/{len(votos)}\n")
print(f"O percentual de votos para o jogador 10 é: {len(jog10)}/{len(votos)}\n")
print(f"O percentual de votos para o jogador 11 é: {len(jog11)}/{len(votos)}\n")

max_votos = max(len(jog7), len(jog8), len(jog9), len(jog10), len(jog11))

print("O melhor jogador foi:")
if len(jog7) == max_votos:
  print(f"Jogador 7 com {len(jog7)} votos ({len(jog7)/len(votos):.2%})")
if len(jog8) == max_votos:
  print(f"Jogador 8 com {len(jog8)} votos ({len(jog8)/len(votos):.2%})")
if len(jog9) == max_votos:
  print(f"Jogador 9 com {len(jog9)} votos ({len(jog9)/len(votos):.2%})")
if len(jog10) == max_votos:
  print(f"Jogador 10 com {len(jog10)} votos ({len(jog10)/len(votos):.2%})")
if len(jog11) == max_votos:
  print(f"Jogador 11 com {len(jog11)} votos ({len(jog11)/len(votos):.2%})")