from abc import ABC


from extra import fim, green, red


class SistemaCadastro(ABC):# arrumado

  def __init__(self, nome, senha, email):
    self.__nome = nome
    self.__email = email
    self.__senha = senha

  def Cadastro(self, lista,objeto) -> None:
    lista.append(objeto)
    print(f'{green}Cadastro feito com sucesso{fim}')
    
  def getNome(self):
    return self.__nome
  def getSenha(self):
    return self.__senha


class Sistemalogin(ABC): #Arrumado

  def __init__(self, nome, senha):
    self.__nome = nome
    self.__senha = senha
    
   
  def verificar(   
      self, lista
  ):  # mudar variavel 'lista' pela de vocês na hora da subclasse

    if len(lista) > 0:
      for c in lista:
        if c.getNome() == self.__nome and c.getSenha() == self.__senha:
          print(f'{green}Login realizado com sucesso{fim}')
          login_sucesso = True
          break

      if not login_sucesso:
        print(f'{red}Valores incorretos{fim}')

    else:
      print(f'{red}Não possue contas no banco dados {fim}')




class CadastroAluno(SistemaCadastro):

  def __init__(self, nome, senha, email):
    super().__init__(nome, senha, email)
    

  def getNome(self):
    return super().getNome()

  def getSenha(self):
    return super().getSenha()

  def Cadastro(self, lista,objeto):
    super().Cadastro(lista,objeto)


class CadastroAdm(SistemaCadastro):#arrumado

  def __init__(self, nome, senha, email,cod = '101'): # cod é a verificação do ADM
    super().__init__(nome, senha, email)
    self.__cod = cod


  def getSenha(self):
    return super().getSenha() 
  
  def getNome(self):
    return super().getNome() 

  def Cadastro(self, lista,objeto):

    cod_adm = input('Informa o numero de ADM: ')
    if cod_adm == self.__cod:
      super().Cadastro(lista,objeto)
    else:
      print(f'{red}Conta não cadastrada no banco de dados{fim}')






class LoginAluno(Sistemalogin):
  def __init__(self, nome, senha):
    super().__init__(nome, senha)
  

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

#lalala