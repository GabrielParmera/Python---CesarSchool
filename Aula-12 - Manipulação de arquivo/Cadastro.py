arquivo = open("Cadastro.txt", 'w', encoding='utf8')
nomes = []
sobrenomes = []
idades = []

n = int(input("N: "))

for i in range(n):
    nome = input("nome: ")
    nomes.append(nome)
    sobrenome = input("sobrenome: ")
    sobrenomes.append(sobrenome)
    idade = int(input("idade: "))
    idades.append(idade)

for i in range(len(nomes)):
    arquivo.write("Nome: " + nomes[i] + " " + sobrenomes[i] + "Idade: " + str(idades[i]) + "\n")

arquivo.close()

arquivo = open("Cadastro.txt", 'r', encoding='utf8')
print(f"Há {n} pessoas cadastradas")
print(arquivo.read())
arquivo.close()


