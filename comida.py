class Comida:
  def __init__(self, valor: int, nome: str, ingredientes: str):
    self.valor = valor
    self.nome = nome
    self.ingredientes = ingredientes

 
class Lanche(Comida):
  def __init__(self, valor: int, nome: str, ingredientes: str, quantidade:int):
    super().__init__(valor, nome, ingredientes)
    self.quantidade = quantidade

 
class Almoco(Comida):
  def __init__(self, valor: int, nome: str, ingredientes: str, precoPorPeso: int, horario: int):
    super().__init__(valor, nome, ingredientes)
    self.precoPorPeso = precoPorPeso
    self.horario = horario