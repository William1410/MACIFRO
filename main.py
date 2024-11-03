'''Informática 2A, POO
Integrantes:  Davi Tavares dos Santos, WILLIAM CAVALCANTE DAMACENO, Júlia Marcelly Braga Belchior, João Vitor Silva Maciel, Layra Vitória Mota Leal'''

from login import LoginAdm,LoginAluno
from cadastro import CadastroAdm, CadastroAluno
from carrinho import Carrinho
from extra import red,fim, clear
from comida import Lanche,Almoco


#teste 
salgadoFrito = Lanche(6,'Salgado Frito','Temos de carne e preseunto e queijo,',1)

refeicao = Almoco(5,'Almoco','coisa ai ',1,0)

aluno = CadastroAluno('davi','1234','usdfsfdsf')
#teste

ADM_conta = []
Aluno_conta = [aluno] # Exemplo de conta




def cadastrar(subclasse,lista: list):

  nome = input('Digite seu nome:')
  senha = input('Digite seu senha:')
  email = input('Digite seu email:')
  objeto_acessor = subclasse(nome, senha, email)
  objeto_acessor.Cadastro(lista,objeto_acessor)
  
def logar(subclasse,lista: list):  

  global objeto_acessor
  nome = input('Informe seu nome:')
  senha = input('Informe sua senha:')
  
  objeto_acessor = subclasse(nome, senha,False)
  objeto_acessor.verificar(lista)

  '''if objeto_acessor.status == True:
      return True
  else:
      pass'''

  


def Interface_principal():
    Usuario_Carrinho = Carrinho()
    while True: 
    
        Interface = input('''Informe uma opção: 
    1. Comida
    2. Bebida
    3. Carrinho
    4. sair
    R: ''')
        
        if Interface == '1':
            Interface_comida = input(''' De comida Temos: 
1.Salgado frito
2.salgado assado
3.Pão de queijo
4.Almoço
R: ''')
            if Interface_comida == '1':
                quantidadeAtual = int(input('Informe a quantidade:'))
                salgadoFrito.alterar_quantidade(quantidadeAtual)
                Usuario_Carrinho.AdicionarItens(salgadoFrito)
            
            elif Interface_comida == '4':
                peso = int(input('Nós informe o peso da sua comida: '))
                horario = int(input('Informe o horário: '))
                refeicao.alterar_peso_horario(peso,horario)
                Usuario_Carrinho.AdicionarItens(refeicao)
            
        elif Interface == '2': #Apenas quando bebida estiver pronto.
            Interface_bebida = input(''' De Bebida Temos: 
1.Coca_cola
2.Água
3.Suco
R: ''')

        elif Interface == '3':
            Usuario_Carrinho.ExibirIntens()  
        elif Interface == '4':
            break

        else:
            print('Valor invalido.')
    





def menu():
    global objeto_acessor, ADM_conta, Aluno_conta, clear, finalizar

    while True:
        
        print(f'''
{'========== MENU =========='}
Olá, seja bem vindo ao MecIFRO, o que você deseja fazer?
1. Cadastrar 
2. Login
''')
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            clear()
            while True:
                print(f'''
{'========== CADASTRO =========='}
1. Cadastrar como aluno
2. Cadastrar como admin
3. Voltar ao menu
                ''')
                escolha = input('Escolha uma opção: ')
                if escolha == '1':
                    clear()
                    print("\n===========CADASTRO DE ALUNO===========")  
                    cadastrar(CadastroAluno, Aluno_conta)

                elif escolha == '2':
                    clear()
                    print("\n===========CADASTRO DE ADMIN===========")
                    cadastrar(CadastroAdm, ADM_conta)

                elif escolha == '3':
                    clear()
                    return menu()
                
                else:
                    break

        elif opcao == '2':
            clear()
            while True:
                print(f'''
{'========== LOGIN =========='}
1. Login como aluno
2. Login como admin
3. Voltar ao menu''')
                alternativa = input('Escolha uma opção: ')
                if alternativa == '1':
                    clear()
                    print("\n===========LOGIN DE ALUNO===========")  
                    logar(LoginAluno, Aluno_conta)
                    if objeto_acessor.status == True:
                        while True: #O aluno fica nessa interface.
                            Interface_principal()
                    else:
                        pass
                    







                elif alternativa == '2':
                    clear()
                    print("\n===========LOGIN DE ADMIN===========")
                    logar(LoginAdm, ADM_conta)

                elif alternativa == '3':
                    clear()
                    return menu()
                
                else:
                    print(f'{red}Opção inválida. Tente novamente.{fim}')
            
        else:
            print(f'{red}Opção inválida. Tente novamente.{fim}')

menu()

