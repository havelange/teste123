while True:
    entrada = input("Seja bem vindo! Deseja calcular seu IMC? Digite 'Sim' ou 'Não'!")
    if entrada.lower() == 'não' or entrada.lower() == 'nao' or entrada.lower() == 'n':
        print('Até a próxima!')
        break

    if entrada.lower() == 'sim' or entrada.lower() == 's':
        try:
            nome = input('Digite o seu nome!').capitalize()
            peso = float(input(f'{nome}, digite o seu Peso em KG! (ex: 72.5)'))
            altura = float(input(f'{nome}, digite sua altura em M! (ex:1.83)'))

            imc = peso / altura ** 2
            
            if imc <= 18.5:
                resultado_imc = 'Abaixo do peso'
            elif imc <= 24.9:
                resultado_imc = 'Com o peso normal'
            elif imc <= 29.9:
                resultado_imc = 'Sobrepeso'
            else:
                resultado_imc = 'Obeso'


            print(f'{nome}, seu IMC é {imc:.1f}, você está {resultado_imc}')

        except ValueError:
            print(f"Algo deu errado, tente novamente! (Use '.' ao invés de ',')")