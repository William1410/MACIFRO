from abc import ABC


class Comida(ABC):
  def __init__(self, valor: int, nome: str, ingredientes: str):
    self.valor = valor
    self.nome = nome
    self.ingredientes = ingredientes

  


 
class Lanche(Comida):
  def __init__(self, valor: int, nome: str, ingredientes: str, quantidade:int):
    super().__init__(valor, nome, ingredientes)
    self.quantidade = quantidade
    self.valor_final = self.valor * self.quantidade
  
  def alterar_quantidade(self,quantidade):
    self.quantidade = quantidade


 
class Almoco(Comida):
  def __init__(self, valor: int, nome: str, ingredientes: str, Peso: int, horario: int):
    super().__init__(valor, nome, ingredientes)
    self.Peso = Peso
    self.valor_final = Peso*valor
    self.horario = horario
  
  def alterar_peso_horario(self,pesoAtual,horarioAtual):
    self.valor = pesoAtual
    self.horario = horarioAtual


