import random
# --- ALGORITMO 6: WS-CLOCK (Shayra) ---

def algoritmo_ws_clock(matriz_ram, ponteiro_atual):
    
    num_paginas = len(matriz_ram) # 10 paginas

    # Loop do relógio: continua girando até achar uma vítima
    while True:
        pagina_candidata = matriz_ram[ponteiro_atual]

        # --- PASSO 1: Checa o bit R ---
        if pagina_candidata.R == 1:
            # R=1: Página usada. Ganha "segunda chance".
            pagina_candidata.R = 0
            # Avança o ponteiro
            ponteiro_atual = (ponteiro_atual + 1) % num_paginas
            continue # Vai para a próxima página
        
        # --- PASSO 2: Se R == 0, checa a "idade" (Obs 3) ---
        else:
            # R=0: Página não usada. Verificar se é "velha".
            
            # Sorteia o Envelhecimento da Página (EP)
            EP = random.randint(100, 9999)
            T_pagina = pagina_candidata.T

            # Compara EP com o T da página
            if EP <= T_pagina:
                # Página "jovem" (ainda no working set).
                # Não substituir. Apenas avançar o ponteiro.
                ponteiro_atual = (ponteiro_atual + 1) % num_paginas
                continue # Vai para a próxima página
            
            else: # (EP > T_pagina)
                # Página "velha" (fora do working set).
                # ENCONTRAMOS A VÍTIMA!
                
                vitima_idx = ponteiro_atual
                proximo_ponteiro = (ponteiro_atual + 1) % num_paginas
                
                # Retorna o índice da vítima e o próximo ponteiro
                return vitima_idx, proximo_ponteiro