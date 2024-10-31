class Carrinho:
    def __init__(self) -> None:
        self.__lista_carrinho = {'cavalo': 2}
    
    def ExibirIntens(self):
        if len(self.__lista_carrinho) == 0:
            print('Não há itens no seu carrinho.')

        else:
            for chave,valor in self.__lista_carrinho.items():
                print(f'{chave} : {valor}')


    def AdicionarItens(self,chave, valor):

        self.__lista_carrinho[chave] = valor


teste = Carrinho()
teste.ExibirIntens()

teste.AdicionarItens('doido',3)
teste.ExibirIntens()