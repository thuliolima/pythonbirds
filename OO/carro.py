NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'

class direcao:
    rotacao_direita = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rotacao_esquerda = {NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE}

    def __init__(self):
        self.valor = NORTE
    def girar_direita(self):
        self.valor = self.rotacao_direita[self.valor]
    def girar_esquecerda(self):
        self.valor = self.rotacao_esquerda[self.valor]

class motor:
    def __init__(self):
        self.valocidade = 0

    def acelerar(self):
        self.valocidade = +1

    def freiar(self):
        self.valocidade -=2
        self.valocidade = max(0, self.valocidade)
