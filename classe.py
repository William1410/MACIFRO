


from extra import fim, green, red


class SistemaCadastro:

  def __init__(self, nome, senha, email):
    self.nome = nome
    self.email = email
    self.senha = senha

  def Cadastro(self, dicionario) -> None:
    if dicionario.get(self.nome) is not None:
      if dicionario[self.nome][0] == self.senha:
        print(f'{red}Usuario já existente{fim}')

    else:
      print(f'{green}Cadastro Realizado{fim}')
      dicionario[self.nome] = [self.senha, self.email]


class Sistemalogin:

  def __init__(self, nome, senha):
    self.nome = nome
    self.senha = senha

  def verificar(
      self, dicionario
  ):  # mudar variavel 'dicionario' pela de vocês na hora da subclasse

    if dicionario.get(self.nome) is not None:
      if dicionario[self.nome][0] == self.senha:

        print(f'{green}Login realizado com sucesso{fim}')

      else:
        print(f'{red}Valores invalidos{fim}')

    else:
      print('Usuario inexistente')


class CadastroAluno(SistemaCadastro):

  def __init__(self, nome, senha, email):
    super().__init__(nome, senha, email)
    

  def Cadastro(self, dicionario):
    super().Cadastro(dicionario)


class CadastroAdm(SistemaCadastro):

  def __init__(self, nome, senha, email):
    super().__init__(nome, senha, email)

  def Cadastro(self, dicionario):
    cod = 101
    cod_adm = int(input('Informa o numero de ADM: '))
    if cod_adm == cod:
      super().Cadastro(dicionario)
    else:
      print('Incorreto')