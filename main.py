from classe import LoginAdm, CadastroAluno, CadastroAdm,LoginAluno
from extra import red, green, fim, clear



ADM_conta = []
Aluno_conta = [] # Exemplo de conta


def cadastrar(subclasse,lista):

  print(f'''
{'==========CADASTRO=========='}
''')
  nome = input('Digite seu nome:')
  senha = input('Digite seu senha:')
  email = input('Digite seu email:')
  objeto_acessor = subclasse(nome, senha, email)
  objeto_acessor.Cadastro(lista,objeto_acessor)
  
def logar(subclasse,lista):  

  global objeto_acessor
  print(f'''
{'==========Login=========='}
''')
  nome = input('Informe seu nome:')
  senha = input('Informe sua senha:')
  objeto_acessor = subclasse(nome, senha)
  objeto_acessor.verificar(lista)


print('ADM BOSTA')
cadastrar(CadastroAdm,ADM_conta)
logar(LoginAdm,ADM_conta)

print('Aluno bosta')
cadastrar(CadastroAluno,Aluno_conta)
logar(LoginAluno,Aluno_conta)


