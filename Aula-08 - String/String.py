frase = 'Apenas um teste!'
print(len(frase)) #Conta o tamanho da string
print('Apen' in frase) #Verifica se a string contém a palavra
print('vish' in frase)
#Concentração de strings para saída de dados#
nome = "Luís"
sobrenome = "Durma mais"
print(f"{nome}, {sobrenome}")
print(nome, sobrenome)
print(nome + ", " + sobrenome)
print("{}, {}".format(nome, sobrenome))
#Transformação#
teste = 'vish, essa semana tem evento!'
novo_teste = teste.replace('vish', 'opa')
print(novo_teste)

caso = 'Sorria, Hoje é segunda!'
print(caso.upper()) #Tudo maiúsculo
print(caso.lower()) #Tudo minúsculo
print(caso.title()) #Primeira letra de cada palavra maiúscula
print(caso.capitalize()) #Apenas a primeira letra da frase maiúscula
print(caso.count('Hoje'))

eita = 'apenas fazendo um teste'
print(eita.split()) #Cria lista de string
print(eita.strip()) #Remove espaços em branco
print(eita.lstrip()) #Remove espaço em branco da esquerda
print(eita.rstrip()) #Remove espaço em branco de direita

Time = ['Rafael', 'Carlos', 'Lucas', 'Luís']
print(Time)
print(", ".join(Time)) #Usando quando string está em uma lista
print(" - ".join(Time))