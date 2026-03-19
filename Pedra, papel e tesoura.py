import random
import time
elementos = ['pedra', 'papel', 'tesoura']
regras_jogo = {'pedra':'tesoura', 'papel':'pedra', 'tesoura':'papel'}


nome = input('Bem-vindo, digite o nome do jogador.').capitalize().strip()


while True:
    intro = input(f"{nome}, deseja jogar pedra, papel e tesoura? Se sim, digite 'sim', senão digite 'não'")

    if intro.lower().strip() in ['n', 'nao', 'não', 'nn']: # SAI DO JOGO
        print(f"Adeus, {nome}!")
        time.sleep(1)
        exit()

    elif intro.lower().strip() in ['sim', 's', 'ss', 'sin']: # PROSSEGUE PARA A PRÓXIMA PARTE
        break

    else:
        print(f"{nome}, ocorreu um erro! Tente novamente, digite apenas 'sim' ou 'não'. Por favor! ")
        time.sleep(2)

time.sleep(2)


while True:
    escolha_pc = random.choice(elementos)

    escolha_jogador = input(f'Vamos começar, {nome}? Escolha, pedra, papel ou tesoura!').lower().strip()
    if escolha_jogador not in elementos:
        print(f"{nome}, ocorreu um erro! Tente novamente, digite apenas 'pedra', 'papel' ou 'tesoura'. Por favor! ")
        time.sleep(2)
        continue

    if regras_jogo[escolha_jogador] == escolha_pc: # VITÓRIA do JOGADOR
        resultado = f'Parabéns! O {nome} venceu o jogo!'

    elif escolha_jogador == escolha_pc: # EMPATE do JOGADOR
        resultado = f'Empate! O {nome} empatou o jogo!'

    else: # DERROTA do JOGADOR
        resultado = f'Derrota! O {nome} perdeu o jogo!'


    print('Pedra....')
    time.sleep(1)
    print('Papel...')
    time.sleep(2)
    print('Tesou...')
    time.sleep(2)
    print('Rá!!')
    time.sleep(2)

    print (f"O {nome} escolheu {escolha_jogador}...")
    time.sleep(2)
    print ('A máquina escolheu...')
    time.sleep(3)
    print ('...')
    time.sleep(1)

    print (f"O computador escolheu {escolha_pc}!")
    time.sleep(2)

    print(f'{resultado}')
    time.sleep(5)

    while True:
        deseja_jogar = input(f'{nome}, deseja jogar novamente? digite sim, senão digite não.')
        if deseja_jogar.lower().strip() in ['sim', 's', 'ss']: # VOLTA PARA O SEGUNDO WHILE
            print('E lá vamos nós!')
            time.sleep(2)
            break
        elif deseja_jogar.lower().strip() in ['n', 'nao', 'não', 'nn']: # SAI DO JOGO
            print(f"Adeus, {nome}, até a próxima!")
            time.sleep(1)
            exit()
        else:
            print(f"{nome}, ocorreu um erro! Tente novamente, digite apenas 'sim' ou 'não'. Por favor! ")
            time.sleep(2)
