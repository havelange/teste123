while True:
    entrada = input("Digite um número ou digite 'sair'.")
    if entrada.lower() == 'sair':
        print('Encerrando...')
        break

    numero = int(entrada)
    if numero % 2 == 0:
        print(f'{numero} é um número par.')
    else:
        print (f'{numero} é um número ímpar')



