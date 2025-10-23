def processar_frase(frase, maior_palavra):
    """
    Processa uma frase e retorna o padrão de tamanhos e a possível nova maior palavra
    """
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Lista para armazenar o tamanho de cada palavra
    tamanhos = []
    
    # Processa cada palavra da frase
    for palavra in palavras:
        # Adiciona o tamanho da palavra à lista
        tamanhos.append(str(len(palavra)))
        
        # Atualiza a maior palavra se necessário
        if len(palavra) >= len(maior_palavra):
            maior_palavra = palavra
    
    # Retorna o padrão de tamanhos e a maior palavra atual
    return "-".join(tamanhos), maior_palavra

def main():
    # Inicializa variáveis
    maior_palavra = ""
    resultados = []
    
    while True:
        # Lê uma linha de entrada
        entrada = input()
        
        # Verifica se é o fim da entrada
        if entrada == "0":
            break
        
        # Processa a frase atual
        padrao, maior_palavra = processar_frase(entrada, maior_palavra)
        resultados.append(padrao)
    
    # Imprime todos os resultados
    for resultado in resultados:
        print(resultado)
    
    # Imprime a maior palavra
    print(f"\nThe biggest word: {maior_palavra}")

# Executa o programa
if __name__ == "__main__":
    main()
