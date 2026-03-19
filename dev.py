lista = []

def menu():
    while True:
        try:
            print('Digite 1 para verificar a lista\nDigite 2 para adicionar algo à lista\nDigite 3 para remover algo da lista.\nDigite 4 para sair.')
            entradamenu = int(input())

            if entradamenu == 1:
                verificar()
            
            elif entradamenu == 2:
                adicionar()

            elif entradamenu == 4:
                print('Encerrando programa...')
                break

            elif entradamenu == 3:
                remover()

        except ValueError:
            print('Digite apenas números.')
            continue

def verificar():
    while True:
        print(',\n'.join(lista))
        input('Digite enter para voltar para o menu.')
        return
    
def adicionar():
    while True:
            print('Digite o que você deseja adicionar na lista.')
            adicionar = input().capitalize().strip()

            if adicionar in lista:
                print('Item já adicionado na lista, retornando ao menu...')
                return
            
            else:
                lista.append(adicionar)
                print('Item adicionado! Retornando ao menu...')
                return
            
def remover():
    while True:
        print ('Digite o nome do que você deseja remover.')
        print (',\n'.join(lista))

        removendo = input()

        if removendo in lista:
            lista.remove(removendo)
            print('Objeto removido com sucesso, retornando...')
            return

        else:
            print('Item não encontrado, retornando...')
            return

menu()