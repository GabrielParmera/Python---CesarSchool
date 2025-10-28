file = open("Cães_cadastro.txt", "w",encoding="utf8")
nome = []
raca = []

for i in range(2):
    nm = input("Nome do animal: ")
    ra = input("Raça do animal: ")
    nome.append(nm)
    raca.append(ra)

for i in range(len(nome)):
    file.write("Nome: " + nome[i] + " " + "Raça: " + raca[i] + "\n")

file.close()

file = open("Cães_cadastro.txt", 'r', encoding='utf8')
print("\n-----Animais Cadastrados-----\n")
print(file.read())
file.close()