import os
os.system("cls")

harry=0
hermione=0
branco=0
total_votes=0
porcen=0.0

while (True):
    print("Quem você vota para presidente?")
    print("[1] - Harry Potter")
    print("[2] - Hermione Granger")
    print("[3] - Voto em branco")
    print("[4] - Sair da votação")
    voto = int(input("Digite o seu voto: "))

    if voto == 1:
        harry+=1
        total_votes += 1
    elif voto == 2:
        hermione+=1
        total_votes += 1
    elif voto == 3:
        branco+=1
        total_votes += 1
    elif voto == 4:
        break
    else:
        print("Opção inválida. Tente novamente.")
        continue

print(f"\nHarry teve {harry} votos.")
print(f"\nHermione teve {hermione} votos.")
print(f"\nTeve {branco} votos brancos.")
if total_votes > 0:
    porcen = (branco / total_votes) * 100
else:
    porcen = 0.0

print(f"\nForam {porcen:.2f}% votos brancos.")

if harry > hermione:
    print("Vencedor: Harry Potter")
elif hermione > harry:
    print("Vencedora: Hermione Granger")
else:
    if harry == 0 and hermione == 0 and branco == 0:
        print("Nenhum voto registrado.")
    else:
        print("Empate entre Harry e Hermione.")
