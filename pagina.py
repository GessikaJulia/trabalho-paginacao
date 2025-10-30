# Define a classe Pagina
# Tem todos os campos da especificacao (N, I, D, R, M, T)
class Pagina:
    def __init__(self, N=-1, I=-1, D=0, R=0, M=0, T=0):
        self.N = N  # Numero da Pagina (0-99)
        self.I = I  # Instrucao (1-100)
        self.D = D  # Dado
        self.R = R  # Bit de Acesso
        self.M = M  # Bit de Modificacao
        self.T = T  # Tempo de Envelhecimento

        # Campo extra pro LRU
        self.ultimo_acesso = 0 

    # Funcao pra imprimir formatado no console
    def __str__(self):
        return f"[N: {self.N:2} | I: {self.I:3} | D: {self.D:3} | R: {self.R} | M: {self.M} | T: {self.T:4} | Ultimo Acesso: {self.ultimo_acesso:4}]"