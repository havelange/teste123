while True:
    entrada = input('Digite o multiplicando ou escreva "sair".')
    if entrada.lower() == "sair":
        print('Adeus!')
        break

    try:
        multiplicando = int(entrada)
        segunda_variavel = input(f'Digite o multiplicador')
        multiplicador = int(segunda_variavel)
        resultado = multiplicador * multiplicando
        print(f'O resultado de {multiplicando} vezes {multiplicador} é igual a {resultado}')
        print('-' * 30)
    except ValueError:
        print("Inválido, tente novamente.")