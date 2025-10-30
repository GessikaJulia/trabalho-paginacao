# --- ALGORITMO 1: FIFO (Gessika) ---

def algoritmo_fifo(matriz_ram, ponteiro_atual):
    indice_vitima = ponteiro_atual
    
    proximo_ponteiro = (ponteiro_atual + 1) % 10 
    
    return indice_vitima, proximo_ponteiro