nomes = []

while True:
    print("\nMenu:")
    print("1. Adicionar nome")
    print("2. Listar nomes")
    print("3. Atualizar nome")
    print("4. Deletar nome")
    print("5. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome a ser adicionado: ")
        nomes.append(nome)
    elif opcao == 2:
        print("Lista de nomes:")
        for n, nome in enumerate(nomes):
            print(f"- {n}: {nome}")
    elif opcao == 3:
        indice = int(input("Digite o índice do nome a ser atualizado: "))
        if 0 <= indice < len(nomes):
            novo_nome = input("Digite o novo nome: ")
            nomes[indice] = novo_nome
        else:
            print("Índice inválido.")
    elif opcao == 4:
        indice = int(input("Digite o índice do nome a ser deletado: "))
        if 0 <= indice < len(nomes):
            nomes.pop(indice)
        else:
            print("Índice inválido.")
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
