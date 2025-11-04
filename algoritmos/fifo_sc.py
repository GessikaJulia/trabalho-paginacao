# --- ALGORITMO 2: FIFO-SC (Liliany) ---
# ---------------------------------------------------------------

def algoritmo_fifo_sc(matriz_ram, ponteiro_atual):
    """
    Implementação do algoritmo FIFO com Segunda Chance.
    Usa o bit R para decidir se uma página ganha 'segunda chance'.
    """
    num_paginas = len(matriz_ram)

    while True:
        pagina = matriz_ram[ponteiro_atual]

        # Caso o bit R seja 0, a página será substituída
        if pagina.R == 0:
            vitima_idx = ponteiro_atual
            ponteiro_atual = (ponteiro_atual + 1) % num_paginas  # Avança circularmente
            return vitima_idx, ponteiro_atual

        # Caso o bit R seja 1, dá uma segunda chance
        else:
            pagina.R = 0  # Zera o bit R
            # Move o ponteiro pra próxima posição circular
            ponteiro_atual = (ponteiro_atual + 1) % num_paginas
            # Continua o loop até achar uma página R=0
