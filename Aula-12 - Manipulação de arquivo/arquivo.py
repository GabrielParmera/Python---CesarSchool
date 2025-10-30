file = open("exemplo_texto_plano.txt", "w") #Coloca o nome do documento
#r -> leitura
#w -> Usado para escrever, também cria o documento referenciado se ele não existir
#a ->

#write -> grava uma string no arquivo por vez
#write

for i in range(5):
    nome = input()
    sobrenome = input()
    idade = int(input())
    file.write(nome) #até aqui fica tudo na mesma linha
    file.write(nome + " " + sobrenome + str(idade) +"\n") #concatenação ->Separa por espaço e separa por linha
    #necessário converter idade p/ string
# lista = []
#for i in range(len(lista)):
#    file.write(nome[i] + " " + sobrenome[i] + " " + str(idade[i])) + "\n")



file.close #para fechar