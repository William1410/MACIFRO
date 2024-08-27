from classe import LoginAdm, CadastroAluno, CadastroAdm
from extra import red, green, fim, clear


objeto_acessor = LoginAdm(' ',' ',' ')
objeto_acessor2 = CadastroAdm(' ', ' ', ' ')

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





cadastrar(CadastroAdm)
objeto_acessor2.Cadastro(ADM_conta)
logar(LoginAdm)
objeto_acessor.verificar(ADM_conta)
print(f'/n/n {ADM_conta}')

