class Pessoa:
    #atributo de class
    olhos = 2
    def __init__(self, *filhos, name=None, idade=29):
        self.name = name
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá{id(self)}'

    @staticmethod
    def metodo_estatic():
        return 10 + 10

    @classmethod
    def nome_e_atributos_da_classe(cls):
        return f'{cls} = olhos {cls.olhos}'

if __name__ == '__main__':
    nicolas = Pessoa(name='Nicolas')
    thulio = Pessoa(nicolas, name="Thulio")
    print(thulio.filhos)

    # Criação do atributo dinamico
    thulio.sobrenome = "Lima"
    print(thulio.sobrenome)
    print(thulio.__dict__)

    del thulio.sobrenome

    print(thulio.__dict__)

    print(Pessoa.olhos)

    Pessoa.olhos = 3

    print(Pessoa.olhos)

    for filhos in thulio.filhos:
        print(filhos.name)

    print(Pessoa.metodo_estatic(), thulio.metodo_estatic())
