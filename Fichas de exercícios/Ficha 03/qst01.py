def obter_vencedor(rajesh, sheldon):
    if rajesh == sheldon:
        return "empate"
    
    regras = {
        "tesoura": ["papel", "lagarto"],
        "papel": ["pedra", "spock"],
        "pedra": ["lagarto", "tesoura"],
        "lagarto": ["spock", "papel"],
        "spock": ["tesoura", "pedra"]
    }
    
    if sheldon in regras[rajesh]:
        return "rajesh"
    else:
        return "sheldon"

C = int(input())

resultados = []

for _ in range(C):
    rajesh, sheldon = input().split()
    
    vencedor = obter_vencedor(rajesh.lower(), sheldon.lower())
    resultados.append(vencedor)

for resultado in resultados:
    print(resultado)
