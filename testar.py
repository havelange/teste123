users = []

def menu():
    while True:
        print("Digite '1' para Acessar sua conta  \n Digite '2' para Criar uma conta \n Digite '3' para Sair")
        print()

        try:
            digito = int(input("Insira o dígito: "))

            if digito == 1:
                menulogin()

            elif digito == 2:
                print()
                menusignup()

            elif digito == 3:
                print('Encerrando programa. . .')
                exit()

            else:
                print("Ops! Dígito inválido, tente novamente.")
                print()
                continue
        except ValueError:
            print("Ops! Digite apenas números, tente novamente.")
            print()
            continue

def menusignup():
    while True:
        usuario = input("Crie seu nome de usuário, (máximo de 10 carácteres: ").lower().strip()
        senha = input("Crie sua senha, (máximo de 10 carácteres: ")
        senha_confirmar = input("Repita sua senha: ")

        if len(senha) > 10 or len(usuario) > 10:
            print("Ops! Limite de dígitos excedido, tente novamente.")
            continue

        elif usuario in users:
            print("Ops! Nome de usuário já utilizado, tente novamente.")
            continue

        elif senha_confirmar != senha:
            print("Ops! As senhas não coincidem, tente novamente.")
            continue

        else: 
            contanova = {"usuario": usuario, "senha":senha}
            users.append(contanova)
            print('Conta criada com sucesso!')
            break

def menulogin():
    while True:
        usuario = input("Digite seu nome de usuário: ").lower().strip()
        senha = input("Digite sua senha: ")

        usuario_procurar = None
        for conta in users:
            if conta["usuario"] == usuario:
                usuario_procurar = conta
                break
             
        if usuario_procurar["senha"] == senha:
            areadouser()

        elif usuario_procurar is None:
            print('Ops! Usuário não encontrado, crie uma conta para acessar.')
            break

        if usuario_procurar["senha"] != senha:
            print('Ops! Senha incorreta, tente novamente.')
        else: 

            print('Ops! Erro não identificado, tente novamente.')
            break