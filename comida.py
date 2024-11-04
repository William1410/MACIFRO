from abc import ABC


class Comida(ABC):
  def __init__(self, valor: int, nome: str, ingredientes: str):
    self.__valor = valor
    self.nome = nome
    self.ingredientes = ingredientes

  def get_valor(self):
    return self.__valor


  def set_valor(self,NovoValor):
    self.__valor = NovoValor
    
class Lanche(Comida):
  def __init__(self, valor: int, nome: str, ingredientes: str, quantidade:int):
    super().__init__(valor, nome, ingredientes)
    self.qtd = quantidade
    self.valor_final = self.get_valor() * self.qtd
  
  def get_valor(self):
    return super().get_valor()

  def atualizar(self):
    self.valor_final = self.get_valor() * self.qtd

  def set_valor(self, NovoValor):
    super().set_valor(NovoValor)



class Almoco(Comida):
  def __init__(self, valor: int, nome: str, ingredientes: str, Peso: int, horario: int):
    super().__init__(valor, nome, ingredientes)
    self.Peso = Peso
    self.horario = horario
    self.valor_final = self.get_valor() * self.Peso
  
  def get_valor(self):
    return super().get_valor()

  def atualizar(self):
    self.valor_final = self.get_valor() * self.Peso

  def set_valor(self, NovoValor):
    super().set_valor(NovoValor)



