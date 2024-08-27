


from extra import fim, green, red


class SistemaCadastro:# arrumado

  def __init__(self, nome, senha, email):
    self.nome = nome
    self.email = email
    self.senha = senha

  def Cadastro(self, lista,objeto) -> None:
    lista.append(objeto)
    print(f'{green}Cadastro feito com sucesso{fim}')
    


class Sistemalogin: #Arrumado

  def __init__(self, nome, senha):
    self.nome = nome
    self.senha = senha

  def verificar(
      self, lista
  ):  # mudar variavel 'lista' pela de vocês na hora da subclasse

    if len(lista) > 0:
      for c in lista:
          
        if c.nome == self.nome and c.senha == self.senha:

          print(f'{green}Login realizado com sucesso{fim}')
          
        else:
          print('f{red}Valores incorretos{fim}')

    else:
      print(f'{red}Não possue contas no banco dados {fim}')









class CadastroAluno(SistemaCadastro):

  def __init__(self, nome, senha, email):
    super().__init__(nome, senha, email)
    

  def Cadastro(self, lista,objeto):
    super().Cadastro(lista,objeto)


class CadastroAdm(SistemaCadastro):#arrumado

  def __init__(self, nome, senha, email,cod = '101'): # cod é a verificação do ADM
    super().__init__(nome, senha, email)
    self.cod = cod

  def Cadastro(self, lista,objeto):

    cod_adm = input('Informa o numero de ADM: ')
    if cod_adm == self.cod:
      super().Cadastro(lista,objeto)
    else:
      print('Incorreto')






class LoginAluno(Sistemalogin):
  def __init__(self, nome, senha):
    super().__init__(nome, senha)
  
  def verificar(self, lista):
    super().verificar(lista)

  
class LoginAdm(Sistemalogin):#Arrumado
  def __init__(self, nome, senha,cod = '101'):
    super().__init__(nome, senha)
    self.cod = cod

  def verificar(self, lista) -> None:
    cod_adm = input('Informe o cod de ADM:')

    if cod_adm == self.cod:
      super().verificar(lista)

    else:
      print(f'{red}Codigo invalido{fim}')
