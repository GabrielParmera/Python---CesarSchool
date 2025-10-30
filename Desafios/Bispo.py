def alg_para_coords(pos_alg):
    """Converte uma posição em notação algébrica (e.g., 'a1') para coordenadas (linha, coluna)."""
    col = ord(pos_alg[0]) - ord('a')
    linha = 8 - int(pos_alg[1])
    return (linha, col)

def coords_para_alg(linha_col):
    """Converte coordenadas (linha, coluna) para notação algébrica (e.g., 'a1')."""
    linha, col = linha_col
    col_alg = chr(ord('a') + col)
    linha_alg = str(8 - linha)
    return col_alg + linha_alg

def encontrar_primeira_capturavel_na_direcao(pos_bispo, pecas_inimigas, dl, dc):
    """
    Percorre uma diagonal a partir da posição do bispo em uma direção específica
    e retorna a primeira peça inimiga capturável encontrada nessa direção, se existir.

    Args:
        pos_bispo: Uma tupla (linha, coluna) representando a posição do bispo.
        pecas_inimigas: Uma lista de tuplas (linha, coluna) representando as posições das peças inimigas.
        dl: A variação na linha para a direção (e.g., -1 para cima, 1 para baixo).
        dc: A variação na coluna para a direção (e.g., -1 para esquerda, 1 para direita).

    Retorna:
        Uma tupla (linha, coluna) da peça capturável, ou None se nenhuma peça for encontrada.
    """
    tamanho_tabuleiro = 8
    linha_bispo, col_bispo = pos_bispo
    linha, col = linha_bispo + dl, col_bispo + dc

    while 0 <= linha < tamanho_tabuleiro and 0 <= col < tamanho_tabuleiro:
        if (linha, col) in pecas_inimigas:
            return (linha, col)
        linha, col = linha + dl, col + dc

    return None


def encontrar_pecas_capturaveis(pos_bispo, pecas_inimigas):
    """
    Determina quais peças inimigas podem ser capturadas por um bispo em um único lance
    utilizando uma função parametrizada para verificar cada diagonal.

    Args:
        pos_bispo: Uma tupla (linha, coluna) representando a posição do bispo.
        pecas_inimigas: Uma lista de tuplas (linha, coluna) representando as posições das peças inimigas.

    Retorna:
        Uma lista de tuplas (linha, coluna) das peças inimigas que podem ser capturadas.
    """
    capturaveis = []
    # Define as 4 direções diagonais
    direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dl, dc in direcoes:
        primeira_capturavel = encontrar_primeira_capturavel_na_direcao(pos_bispo, pecas_inimigas, dl, dc)
        if primeira_capturavel:
            capturaveis.append(primeira_capturavel)

    return capturaveis


# Leitura da entrada
bispo_alg = input("Escreva a posição do bispo:")
n = int(input("Número de peças inimigas: "))
lista_pecas_inimigas_alg = [input("Posição das peças inimigas, um por linha: ") for _ in range(n)]

# Conversão para coordenadas
posicao_bispo = alg_para_coords(bispo_alg)
posicoes_inimigas = [alg_para_coords(pos) for pos in lista_pecas_inimigas_alg]

# Encontra as peças capturáveis
pecas_capturaveis_coords = encontrar_pecas_capturaveis(posicao_bispo, posicoes_inimigas)

# Converte as coordenadas das peças capturáveis de volta para notação algébrica
pecas_capturaveis_alg = [coords_para_alg(coords) for coords in pecas_capturaveis_coords]

# Ordena as posições capturáveis lexicograficamente
pecas_capturaveis_alg.sort()

# Gera a saída no formato especificado
k = len(pecas_capturaveis_alg)
print(k)
if k > 0:
    print(" ".join(pecas_capturaveis_alg))