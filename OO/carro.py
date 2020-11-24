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

class carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.valocidade

    def velocidade(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.freiar()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.girar_a_direita()
    def girar_a_esquerda(self):
        return self.girar_a_esquerda()
