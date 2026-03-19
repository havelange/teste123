while True:
    entrada = input("Digite o número para averiguar a tábuada. Ou digite 'sair'")

    if entrada.lower() == 'sair':
        print ('Adeus, Claude!')
        break

    try:
        n = int(entrada)
        for i in range(1,11):
            resultado = n*i

            print(f'{n} vezes {i} é igual a {resultado}.')

    except ValueError:
        print("Inválido, tente novamente.")

print ('-' * 30)
