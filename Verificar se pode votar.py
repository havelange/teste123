while True:
    entrada = input("Digite um número ou digite 'sair'.")
    if entrada.lower() == 'sair':
        print('Encerrando Programa.')
        break

    numero = int(entrada) 
    if numero <= 15:
        print(f'Com {numero} anos, você não pode votar.')
    elif numero <= 17:
        print(f'Com {numero} anos, você pode votar, porém é facultativo.')
    elif numero <= 69:
        print(f'Com {numero} anos, você pode votar.')
    elif numero >= 70:
        print(f'Com {numero} anos, você pode votar, porém é facultativo.')