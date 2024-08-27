from classe import Sistemalogin, CadastroAluno, CadastroAdm
from extra import red, green, fim, clear

codigo = 101

objeto_acessor = Sistemalogin(' ',' ')
objeto_acessor2 = CadastroAluno(' ', ' ', ' ')

ADM_conta = {}
Aluno_conta = {'Davi': ['1234', 'Davifghk11@gmail.com']}  # Exemplo de conta


def cadastrar(subclasse):

  global objeto_acessor2
  print(f'''
{'==========CADASTRO=========='}
''')
  nome = input('Digite seu nome:')
  senha = input('Digite seu senha:')
  email = input('Digite seu email:')
  objeto_acessor2 = subclasse(nome, senha, email)


def logar(subclasse):

  global objeto_acessor
  print(f'''
{'==========Login=========='}
''')
  nome = input('Informe seu nome:')
  senha = input('Informe sua senha:')
  objeto_acessor = subclasse(nome, senha)


cadastrar(CadastroAluno)
objeto_acessor2.Cadastro(Aluno_conta)
logar(Sistemalogin)
objeto_acessor.verificar(Aluno_conta)

