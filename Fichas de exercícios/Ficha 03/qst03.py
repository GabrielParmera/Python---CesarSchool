alimentos_vitamina_c = {
    "suco de laranja": 120,
    "morango fresco": 85,
    "mamao": 85,
    "goiaba vermelha": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34
}

recomendado_min = 110
recomendado_max = 130

print("Digite a entrada (T, seguido por T linhas de quantidade e alimento. Digite 0 para terminar):")

while True:
    total_vitamina_c = 0
    num_alimentos = int(input())

    if num_alimentos == 0:
        break

    for _ in range(num_alimentos):
        linha = input()
        partes = linha.split(maxsplit=1)
        quantidade = int(partes[0])
        nome_alimento = partes[1].strip() 
        if nome_alimento in alimentos_vitamina_c:
            total_vitamina_c += quantidade * alimentos_vitamina_c[nome_alimento]
        else:
            print(f"Erro: Alimento '{nome_alimento}' não encontrado na tabela de vitamina C. Verifique a digitação.")


    diferenca_min = total_vitamina_c - recomendado_min
    diferenca_max = total_vitamina_c - recomendado_max

    if total_vitamina_c > recomendado_max:
        mensagem_saida = f"Menos {abs(diferenca_max)} mg"
    elif total_vitamina_c < recomendado_min:
        mensagem_saida = f"Mais {abs(diferenca_min)} mg"
    else:
        mensagem_saida = f"{total_vitamina_c} mg"

    print(mensagem_saida)
