users = []

def menu():
    while True:
            try:
                print()
                print('Digite 1 para realizar um cadastro \nDigite 2 para verificar o cadastro \nDigite 0 para encerrar o programa.')
                resposta = int(input())
                if resposta == 1:
                    cadastro()

                elif resposta == 2:
                    verificar()

                elif resposta == 3:
                    print('Encerrando programa...')
                    break
                else:
                    print('Ops! Digito inválido, tente novamente.')
            except ValueError:
                print('Ops! Digite apenas números, tente novamente.')

def cadastro():
    while True:
        print()
        print('Crie seu nome de usuário, máximo de 10 caracteres.')
        nome = input('Nome: ').strip()

        if nome in users:
            print('Ops! Nome já cadastrado, tente novamente.')
            continue

        elif len(nome) > 10:
            print('Ops! Número de caracteres excedido, tente novamente.')
            continue

        else:
            while True:
                print()
                print('Crie sua senha, máximo 10 caracteres.')
                senha = input('Senha: ').strip()
                print('Repita sua senha: ')
                senha_confirmar = input('Senha: ').strip()

                if senha == senha_confirmar:
                        usernovo = {
                            'nome':nome,
                            'senha':senha
                        }

                        users.append(usernovo)
                        print()
                        print('Conta cadastrada com sucesso!')
                        return
                
                if len(senha) > 10:
                            print('Ops! Número de caracteres excedido, tente novamente.')
                            continue
                
                if senha != senha_confirmar:
                        print('Ops! Senhas não coincidem, tente novamente.')
                        continue
                
                else:
                    print ('Ops! Erro não identificado, retornando para o menu.')
                    return
                
def verificar():
     print():