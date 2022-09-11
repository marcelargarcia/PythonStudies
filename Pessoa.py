from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, profissao, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
        else:
            print(f'{self.nome} está comendo {alimento}.')
            # print(self.nome + " está comendo " + alimento)
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
        else:
            self.comendo = False
            print(f'{self.nome} parou de comer.')

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            self.falando = False
            return
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        self.falando = True
        print(f'{self.nome} está falando sobre {assunto}.')

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        self.falando = False
        print(f'{self.nome} parou de falar.')

    def get_ano_nasci(self):
        return self.ano_atual - self.idade
