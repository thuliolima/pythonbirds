class motor:
    def __init__(self):
        self.valocidade = 0

    def acelerar(self):
        self.valocidade = +1

    def freiar(self):
        self.valocidade -=2
        self.valocidade = max(0, self.valocidade)
