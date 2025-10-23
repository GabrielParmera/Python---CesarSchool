def processar_frase(frase, maior_palavra):
    palavras = frase.split()
    
    tamanhos = []
    
    for palavra in palavras:
        tamanhos.append(str(len(palavra)))
        
        if len(palavra) >= len(maior_palavra):
            maior_palavra = palavra
    
    return "-".join(tamanhos), maior_palavra

def main():
    maior_palavra = ""
    resultados = []
    
    while True:
        entrada = input()
        
        if entrada == "0":
            break
        
        padrao, maior_palavra = processar_frase(entrada, maior_palavra)
        resultados.append(padrao)
    

    for resultado in resultados:
        print(resultado)
    
    print(f"\nThe biggest word: {maior_palavra}")

if __name__ == "__main__":
    main()
