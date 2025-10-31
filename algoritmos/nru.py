import random
from pagina import Pagina 

# --- ALGORITMO 4: NRU (Not Recently Used) ---
def algoritmo_nru(matriz_ram: list[Pagina]) -> int:
    
    if not matriz_ram:
        raise ValueError("MATRIZ_RAM não pode estar vazia.")
    
    # 1. Armazena os *índices* (posições 0-9) das páginas em suas classes
    classe_0 = []
    classe_1 = []
    classe_2 = []
    classe_3 = []
    
    # Itera sobre a RAM para classificar cada página
    for idx, pagina in enumerate(matriz_ram):
        if pagina.R == 0 and pagina.M == 0:
            classe_0.append(idx)
        elif pagina.R == 0 and pagina.M == 1:
            classe_1.append(idx)
        elif pagina.R == 1 and pagina.M == 0:
            classe_2.append(idx)
        else: # pagina.R == 1 and pagina.M == 1
            classe_3.append(idx)

    # 2. Encontra a classe de menor prioridade que não esteja vazia
    #    e sorteia uma vítima aleatória *dessa* classe.
    
    if classe_0:
        # A melhor classe para remover (não usada, não suja)
        return random.choice(classe_0)
        
    elif classe_1:
        # Segunda melhor (não usada, mas suja - exige write-back)
        return random.choice(classe_1)
        
    elif classe_2:
        # Terceira melhor (usada, mas limpa)
        return random.choice(classe_2)
        
    elif classe_3:
        # Pior classe (usada e suja)
        return random.choice(classe_3)

    # Substitui o 'return 0' por um erro claro
    # Este caso não deve ser alcançado se a RAM não estiver vazia.
    raise ValueError("Erro no NRU: Nenhuma página encontrada para classificar.")
