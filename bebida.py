class Bebida:
    def __init__(self,nome,descricao,valor,quantidade,ml):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade
        self.ml = ml

def exibir_detalhes (self):
    print(f"Bebida: {self.nome}")
    print(f"descricao:{self.descricao}")
    print(f"valor: R${self.valor:.2f}")
    print(f"quantidade em estoque: {self.quantidade}")
    print(f"volume:{self.ml} ml")

bebida1 = Bebida ("refrigerante", 'refrigerante de cola', 5.00 , 10 , 350)
