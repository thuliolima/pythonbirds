class Pessoa:
    def __init__(self, name=None, idade=29):
        self.name = name
        self.idade = idade


    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    p = Pessoa('Thulio')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.name = "Thulio Lima"
    print(p.name)
    print(p.idade)
