class Pessoa:
    def __init__(self, *filhos, name=None, idade=29):
        self.name = name
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    nicolas = Pessoa(name='Nicolas')
    thulio = Pessoa(nicolas, name="Thulio")
    print(thulio.filhos)
    thulio.sobrenome = "Lima"
    print(thulio.sobrenome)

    for filhos in thulio.filhos:
        print(filhos.name)


