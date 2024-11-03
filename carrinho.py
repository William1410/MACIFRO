
class Carrinho:
    def __init__(self) -> None:
        self.__lista_carrinho = []
    
    def ExibirIntens(self):
        if len(self.__lista_carrinho) == 0:
            print('Não há itens no seu carrinho.')

        else:
            print("Nome: valor: quantidade:")
            for c in self.__lista_carrinho:
                if hasattr(c, 'quantidade'): #verifica se a classe/objeto tem atributo
                    print(f'{c.nome} : {c.valor_final} : {c.quantidade}')
                    

                else:
                    print(f'{c.nome} : {c.valor_final}')
                   


    def AdicionarItens(self,item):
        self.__lista_carrinho.append(item)
