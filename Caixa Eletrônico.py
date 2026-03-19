
#
import time
saldo = 250
#



#
def verificar_saldo():
    while True:
        print("="*38)
        print("="*10, "MENU DE SALDO", "="*10)
        print("="*38)
        print()
        print("Digite '1' para verificar seu Saldo. \nDigite '0' para voltar.")

        try:
            checar_saldo = int(input("Insira o dígito: "))
            if checar_saldo == 0:
                print('Voltando...')
                time.sleep(1.5)
                break

            if checar_saldo == 1:
                verificar_saldo2()

            else:
                print ("Ops! Ocorreu um erro, tente novamente!")
                time.sleep(2)

        except ValueError:
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)
def verificar_saldo2():
    global saldo
    print("="*38)
    print("="*10, "MENU DE SALDO", "="*10)
    print("="*38)
    print()
    print(f"Seu saldo atual é de R${saldo:.2f}")
    time.sleep(2)
    while True:
        try:
            voltar_continuar = int(input("Se deseja voltar para o menu, digite '1', se deseja sair do programa, digite '0': "))
            if voltar_continuar == 1:
                print('Aguarde um momento...')
                time.sleep(2)
                return
            elif voltar_continuar == 0:
                print('Volte sempre!')
                time.sleep(2)
                exit()
            else: 
                print ("Ops! Ocorreu um erro, tente novamente!")
                time.sleep(2)
        except ValueError:
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)
#



#
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
    print("="*38)
    print("="*10, "MENU DE DEPÓSITO", "="*10)
    print("="*38)
    print()
    while True:
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
#



#
def saque_saldo():
    while True:
        print("="*38)
        print("="*10, "MENU DE SAQUE", "="*10)
        print("="*38)
        print()
        print("Digite '1' para realizar um saque. \nDigite '0' para voltar.")

        try:
            realizar_saque = int(input("Insira o dígito: "))
            if realizar_saque == 0:
                print('Voltando...')
                time.sleep(1.5)
                break

            if realizar_saque == 1:
                saque_saldo2()

            else:
                print ("Ops! Ocorreu um erro, tente novamente!")
                time.sleep(2)

        except ValueError:
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)
def saque_saldo2():
    global saldo
    print("="*38)
    print("="*10, "MENU DE SAQUE", "="*10)
    print("="*38)
    print()
    while True:
        try:
            entrada = (input('Digite o valor do saque: ')).strip()
            entrada2  = entrada.replace(',','.')
            valor = float(entrada2)
            valor = round(valor,2)

            if saldo < valor >  0:
                print(f'Não é possível sacar esse valor, pois seu saldo é apenas de R${saldo:.2f}')
                time.sleep(1.66)
            elif valor <= 0:
                print('Não é possível sacar valores menores que zero. Tente novamente!')
                time.sleep(1.66)
            else:
                saldo -= valor 
                time.sleep(1.5)
                print(f'Saque realizado com sucesso! Saldo atualizado: R$ {saldo:.2f}')
                time.sleep(1.5)
                print('Retornando para o menu de saque...')
                time.sleep(1.5)
                break
        except ValueError:
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)  
#



#
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

            if opcao == 1: 
                time.sleep(1.5)
                verificar_saldo()
            elif opcao == 2: 
                time.sleep(1.5)
                deposito_saldo()
            elif opcao == 3: 
                time.sleep(1.5)
                saque_saldo() 
            elif opcao == 0: 
                time.sleep(1.5)
                print("Até a próxima!") 
                time.sleep(1.5)
                break
            else: 
                print ("Ops! Ocorreu um erro, tente novamente!")
                time.sleep(2)
                continue
        except ValueError: 
            print ("Ops! Ocorreu um erro, tente novamente!")
            time.sleep(2)
            continue
#



#
menu()