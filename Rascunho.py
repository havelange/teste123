import time

saldo = 250


def verificar_saldo(): # MENU DE VERIFICAR SALDO
    global saldo
    print(f"Seu saldo atual é de R${saldo:.2f}")
    time.sleep(2)
    while True:
        try:
            voltar_continuar = int(input("Se deseja voltar para o menu, digite '1', se deseja sair do programa, digite '0': "))
            if voltar_continuar == 1: # VOLTAR PARA O MENU
                print('Aguarde um momento...')
                time.sleep(2)
                return
            elif voltar_continuar == 0: # ENCERRAR O PROGRAMA
                print('Volte sempre!')
                time.sleep(2)
                exit()
            else: # DÍGITO INVÁLIDO POR PARTE DO USUÁRIO
                print ("Ops! Ocorreu um erro, tente novamente!")
                time.sleep(2)
        except ValueError: # USUÁRIO USOU LETRA AO INVÉS DE NÚMERO
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)

def deposito_saldo():
    while True:
        print("="*38)
        print("="*10, "MENU DE DEPÓSITO", "="*10)
        print("="*38)
        print()
        print("Digite '1' para realizar um depósito. \nDigite '0' para voltar.")

        try:
            realizar_deposito = int(input("Insira o dígito: "))
            if realizar_deposito == 0:
                print('Voltando...')
                time.sleep(1.5)
                break

            if realizar_deposito == 1:
                deposito_saldo2()

            else:
                print ("Ops! Ocorreu um erro, tente novamente!")
                time.sleep(2)

        except ValueError:
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)
def deposito_saldo2():
    global saldo
    while True:
        print("="*38)
        print("="*10, "MENU DE DEPÓSITO", "="*10)
        print("="*38)
        print()
        
        try:
            entrada = (input('Digite o valor do depósito: ')).strip()
            entrada2  = entrada.replace(',','.')
            valor = float(entrada2)
            valor = round(valor,2)

            if valor > 0:
                saldo += valor 
                time.sleep(1.5)
                print(f'Depósito realizado com sucesso! Saldo atualizado: R$ {saldo:.2f}')
                time.sleep(1.5)
                print('Retornando para o menu de depósito...')
                time.sleep(1.5)
                break
            else:
                print('Valor inválido, tente novamente!')
                time.sleep(1.5)
        except ValueError:
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)    
    
def saque_saldo():

def menu():

    while True:
        print("="*38)
        print("="*10, "CAIXA ELETRÔNICO", "="*10)
        print("="*38)
        print()
        print("Digite '1' para verificar seu saldo. \nDigite '2' para acessar o menu de depósito. \nDigite '3' para acessar o menu de saque. \nDigite '0' para sair.")

        try:
            entrada = int(input("Insira o dígito: "))
            time.sleep(0.5)

            opcao = entrada

            if opcao == 1: # VERIFICAR O SALDO DO USUÁRIO
                time.sleep(1.5)
                verificar_saldo()
            elif opcao == 2: # REALIZAR UM DEPÓSITO NO SALDO DO USUÁRIO
                time.sleep(1.5)
                deposito_saldo()
            elif opcao == 3: # REALIZAR UM SAQUE NO SALDO DO USUÁRIO
                time.sleep(1.5)
                saque_saldo() 
            elif opcao == 0: # ENCERRAR O PROGRAMA 
                time.sleep(1.5)
                print("Até a próxima!") 
                time.sleep(1.5)
                break
            else: # DÍGITO INVÁLIDO POR PARTE DO USUÁRIO
                print ("Ops! Ocorreu um erro, tente novamente!")
                time.sleep(2)
                continue
        except ValueError: # USUÁRIO USOU LETRA AO INVÉS DE NÚMERO
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)
            continue

menu()