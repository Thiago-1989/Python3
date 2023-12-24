from random import randint

print('=' * 40, '\n', ' ' * 12, 'JOKENPO')
print('=' * 40)
print('[1] Pedra  \n[2] Papel \n[3] Tesoura')

jokenpo = ('PEDRA', 'PAPEL', 'TESOURA')

jogador = int(input().strip())

computador = randint(1,2)

print('=' * 40)

if 0 < jogador <= 3:

    print("Computador escolheu {}.".format(jokenpo[computador - 1]))
    print("Jogador escolheu {}.".format(jokenpo[jogador - 1]))
    print('=' * 40)

    if (jogador == 1 and computador == 1) or (jogador == 2 and computador == 2) or (
        jogador == 3 and computador == 3):
        print('\nEmpate!')

    elif (jogador == 1 and computador == 3) or (jogador == 3 and computador == 2) or (
        jogador == 2 and computador == 1):
        print('Jogador venceu!')

    else:
        print('Computador venceu!')

else:
    print('Escolha inválida!')
