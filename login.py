from abc import ABC
from extra import fim, green, red

class Sistemalogin(ABC): #Arrumado

  def __init__(self, nome: str, senha: str, status: bool):
    self.__nome = nome
    self.__senha = senha
    self.status = status
   
  def verificar(self, lista: list):  # mudar variavel 'lista' pela de vocês na hora da subclasse
    if len(lista) > 0:
      for c in lista:
        if c.getNome() == self.__nome and c.getSenha() == self.__senha:
          print(f'{green}Login realizado com sucesso{fim}')
          self.status = True

        else: 
          print(f'{red}Valores incorretos{fim}')
          

    else:
      print(f'{red}Não possue contas no banco dados {fim}')

class LoginAluno(Sistemalogin):
  def __init__(self, nome, senha,status):
    super().__init__(nome, senha,status)
  

  def verificar(self, lista):
    super().verificar(lista)

  
class LoginAdm(Sistemalogin):#Arrumado
  def __init__(self, nome, senha,cod = '101'):
    super().__init__(nome, senha)
    self.__cod = cod

  def verificar(self, lista) -> None:
    cod_adm = input('Informe o cod de ADM:')

    if cod_adm == self.__cod:
      super().verificar(lista)

    else:
      print(f'{red}Codigo invalido{fim}')



teste = LoginAluno('fsdfd','1234',False)
print(teste.status)
