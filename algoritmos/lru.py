# lru.py
"""
Algoritmo de substituição de páginas: LRU (Least Recently Used)
Recebe a matriz RAM (lista de objetos Pagina)
Retorna o índice da página a ser substituída
"""

def algoritmo_lru(matriz_ram):
    """
    Retorna o índice da página a ser substituída usando o LRU.
    """
    # Inicializa com o primeiro índice
    indice_vitima = 0
    ultimo_acesso_min = matriz_ram[0].ultimo_acesso

    # Percorre toda a RAM procurando a página menos recentemente usada
    for idx, pagina in enumerate(matriz_ram):
        if pagina.ultimo_acesso < ultimo_acesso_min:
            ultimo_acesso_min = pagina.ultimo_acesso
            indice_vitima = idx

    return indice_vitima


# ------------------------------
# TESTE RÁPIDO (opcional)
# ------------------------------
if __name__ == "__main__":
    from pagina import Pagina

    # Criar RAM de teste
    ram = [Pagina(N=i, I=i+1) for i in range(10)]

    # Define últimos acessos depois de criar as páginas
    for i, pagina in enumerate(ram):
        pagina.ultimo_acesso = i * 10

    # Modifica alguns últimos acessos para simular acessos recentes
    ram[3].ultimo_acesso = 200
    ram[7].ultimo_acesso = 150

    vitima = algoritmo_lru(ram)
    print(f"Página a ser substituída (menor último acesso): índice {vitima}, N={ram[vitima].N}, último_acesso={ram[vitima].ultimo_acesso}")
