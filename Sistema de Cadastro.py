users = []

def menu():
    while True:
        try:
            print()
            print('Digite 1 para se cadastrar\nDigite 2 para verificar o cadastro\nDigite 3 para listar todos os usuários\nDigite 4 para sair.')
            entrada = int(input())

            if entrada == 1:
                cadastro()
            
            elif entrada == 2:
                verificar()

            elif entrada == 3:
                listausuarios()

            elif entrada == 4:
                print()
                print('Encerrando programa...')
                break

            else:
                print()
                print('Ops! Digito inválido, tente novamente,')
        except ValueError:
            print()
            print('Ops! Digite apenas números!')

def cadastro():
    while True:
        print()
        print('Cadastre seu nome de usuário,\n Máximo de 10 caracteres.')
        nomedeusuario = input().strip().upper()

        if nomedeusuario in users:
            print()
            print('Ops! Usuário já cadastrado, tente novamente.')
            continue
        elif len(nomedeusuario) > 10:
            print()
            print('Ops! Limite de caracteres excedido, tente novamente.')
            continue

        elif len(nomedeusuario) < 1:
            print()
            print('Ops! Mínimo de um caractere, tente novamente.')
        else:
            users.append(nomedeusuario)
            print()
            print('Usuário cadastrado com sucesso!\nRetornando...')
            return
        
def verificar():
    print()
    print('Digite seu nome de usuário')
    verificarnome = input().strip().upper

    if verificarnome in users:
        print()
        print('Usuário encontrado!')
        return
    else:
        print()
        print('Usuário não encontrado! Realize um cadastro ou tente novamente.')    
        return
    
def listausuarios():
    print()
    print(users)
    print()
    input('Pressione enter para voltar para o MENU.')



menu()