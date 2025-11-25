# --- ALGORITMO 3: RELÓGIO (Matheus Ribeiro Silva) ---
def algoritmo_relogio(matriz_ram, ponteiro_atual):
    while True:
        pagina_atual = matriz_ram[ponteiro_atual]

        if pagina_atual.R == 1:
            pagina_atual.R = 0
            ponteiro_atual = (ponteiro_atual + 1) % len(matriz_ram)
        else:
            vitima_idx = ponteiro_atual
            proximo_ponteiro = (ponteiro_atual + 1) % len(matriz_ram)
            return vitima_idx, proximo_ponteiro
