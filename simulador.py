import random
import copy

# Puxa a definicao da Pagina
from pagina import Pagina

# Puxa todos os algoritmos da pasta 'algoritmos'
import algoritmos as alg

# -------------------------------------------------------------------
# FUNCOES DE SETUP (SWAP, RAM, IMPRESSAO)
# (Nao precisa mexer)
# -------------------------------------------------------------------

def inicializar_swap():
    # Cria a SWAP (100 paginas)
    matriz_swap = []
    for i in range(100):
        N = i
        I = i + 1
        D = random.randint(1, 50)
        R = 0
        M = 0
        T = random.randint(100, 9999)
        matriz_swap.append(Pagina(N, I, D, R, M, T))
    return matriz_swap

def inicializar_ram(matriz_swap):
    # Cria a RAM (10 paginas)
    matriz_ram = []
    # Sorteia 10 indices unicos de 0 a 99
    indices_sorteados = random.sample(range(100), 10)
    
    for indice in indices_sorteados:
        # copy.copy() cria um objeto NOVO na RAM
        matriz_ram.append(copy.copy(matriz_swap[indice]))
        
    return matriz_ram

def imprimir_matriz(nome, matriz, limitar_linhas=0):
    # Funcao pra imprimir a RAM ou SWAP
    print(f"\n--- {nome} ---")
    linhas = matriz
    if limitar_linhas > 0:
        linhas = matriz[:limitar_linhas]
        
    for i, pagina in enumerate(linhas):
        print(f"[{i:2}]: {pagina}")

# -------------------------------------------------------------------
# MOTOR DA SIMULACAO
# (Nao precisa mexer)
# -------------------------------------------------------------------

def simular(algoritmo_nome, matriz_ram_inicial, matriz_swap_inicial):
    
    print(f"\n{'='*70}")
    print(f"--- Iniciando Simulacao: {algoritmo_nome} ---")
    print(f"{'='*70}")
    
    # Copia as matrizes pra nao zoar as originais
    MATRIZ_RAM = [copy.copy(p) for p in matriz_ram_inicial]
    MATRIZ_SWAP = [copy.copy(p) for p in matriz_swap_inicial]

    # Ponteiros que alguns algs usam
    ponteiro_fifo = 0
    ponteiro_sc_relogio = 0
    
    page_faults = 0

    # Impressao Inicial (Obs 6)
    print("Estado Inicial da RAM:")
    imprimir_matriz("RAM", MATRIZ_RAM)
    print("\nEstado Inicial da SWAP (primeiras 15):")
    imprimir_matriz("SWAP", MATRIZ_SWAP, 15)

    # Loop principal (Obs 1)
    for i in range(1000):
        instrucao_num_clock = i + 1 
        instrucao_sorteada = random.randint(1, 100) # Sorteia (1-100)
        
        # Tenta achar a pagina na RAM
        pagina_encontrada = None
        for pagina in MATRIZ_RAM:
            if pagina.I == instrucao_sorteada:
                pagina_encontrada = pagina
                break
        
        # --- CASO 1: PAGE HIT ---
        if pagina_encontrada:
            pagina_encontrada.R = 1
            pagina_encontrada.ultimo_acesso = instrucao_num_clock # Pro LRU
            
            # 50% de chance de modificar (Obs 2)
            if random.random() < 0.5:
                pagina_encontrada.D += 1
                pagina_encontrada.M = 1
        
        # --- CASO 2: PAGE FAULT ---
        else:
            page_faults += 1
            
            # 1. Busca pagina na SWAP (I=1 -> N=0, I=100 -> N=99)
            indice_swap = instrucao_sorteada - 1
            nova_pagina = copy.copy(MATRIZ_SWAP[indice_swap])
            nova_pagina.R = 0 
            nova_pagina.M = 0
            nova_pagina.ultimo_acesso = instrucao_num_clock # Pro LRU
            
            # 2. Chama o algoritmo de substituicao (do arquivo certo)
            if algoritmo_nome == "FIFO":
                vitima_idx, ponteiro_fifo = alg.algoritmo_fifo(MATRIZ_RAM, ponteiro_fifo)
            
            elif algoritmo_nome == "FIFO-SC":
                vitima_idx, ponteiro_sc_relogio = alg.algoritmo_fifo_sc(MATRIZ_RAM, ponteiro_sc_relogio)

            elif algoritmo_nome == "RELÓGIO":
                vitima_idx, ponteiro_sc_relogio = alg.algoritmo_relogio(MATRIZ_RAM, ponteiro_sc_relogio)

            elif algoritmo_nome == "NRU":
                vitima_idx = alg.algoritmo_nru(MATRIZ_RAM)

            elif algoritmo_nome == "LRU":
                vitima_idx = alg.algoritmo_lru(MATRIZ_RAM)
                
            elif algoritmo_nome == "WS-CLOCK":
                vitima_idx, ponteiro_sc_relogio = alg.algoritmo_ws_clock(MATRIZ_RAM, ponteiro_sc_relogio)
            
            # 3. Salva na SWAP se M=1 (Write-Back) (Obs 5)
            pagina_vitima = MATRIZ_RAM[vitima_idx]
            if pagina_vitima.M == 1:
                pagina_vitima.M = 0
                MATRIZ_SWAP[pagina_vitima.N] = copy.copy(pagina_vitima)
                
            # 4. Poe a pagina nova na RAM
            MATRIZ_RAM[vitima_idx] = nova_pagina

        # Zera o Bit R a cada 10 instrucoes (Obs 4)
        if instrucao_num_clock % 10 == 0:
            for pagina in MATRIZ_RAM:
                pagina.R = 0

    # --- Fim ---
    print(f"\n--- Fim da Simulacao: {algoritmo_nome} ---")
    print(f"Total de Page Faults: {page_faults}")
    
    # Impressao Final (Obs 6)
    print("\nEstado Final da RAM:")
    imprimir_matriz("RAM", MATRIZ_RAM)
    print("\nEstado Final da SWAP (primeiras 15):")
    imprimir_matriz("SWAP", MATRIZ_SWAP, 15)
    print(f"{'='*70}\n")


# -------------------------------------------------------------------
# MAIN - Onde o programa comeca
# -------------------------------------------------------------------
def main():
    
    # --- CONTROLE ---
    # Mude a string aqui pra testar seu algoritmo
    
    #ALGORITMO_PARA_EXECUTAR = "FIFO"      # (Exemplo pronto)
    #ALGORITMO_PARA_EXECUTAR = "FIFO-SC"   # (TAREFA)
    # ALGORITMO_PARA_EXECUTAR = "RELÓGIO" # (TAREFA)
    # ALGORITMO_PARA_EXECUTAR = "NRU"       # (TAREFA)
    # ALGORITMO_PARA_EXECUTAR = "LRU"       # (TAREFA)
    ALGORITMO_PARA_EXECUTAR = "WS-CLOCK"  # (TAREFA)
    # ----------------

    # Cria as matrizes originais
    swap_original = inicializar_swap()
    ram_original = inicializar_ram(swap_original)

    # Roda a simulacao
    algoritmos_validos = ["FIFO", "FIFO-SC", "RELÓGIO", "NRU", "LRU", "WS-CLOCK"]
    
    if ALGORITMO_PARA_EXECUTAR in algoritmos_validos:
        simular(ALGORITMO_PARA_EXECUTAR, ram_original, swap_original)
    else:
        print(f"ERRO: '{ALGORITMO_PARA_EXECUTAR}' nao eh um nome valido.")
        print(f"Validos sao: {algoritmos_validos}")

# Roda o main() quando o script eh executado
if __name__ == "__main__":
    main()