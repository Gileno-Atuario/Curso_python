# Calculadora com while

def calculadora():

    numero_1 = input('Digite o primeiro número: ')
    try:
        numero_1 = float(numero_1)
    except:
        print('Valor inválido')
        return numero_1

    numero_2 = input('Digite o segundo número: ')
    try:
        numero_2 = float(numero_2)
    except:
        print('Valor inválido')
        return numero_2

    operacao = input('Digite:'
                     '\n\ta para soma'
                     '\n\tb para subtração'
                     '\n\tc para multiplicação'
                     '\n\td para divisão: ')
    operacao = operacao.lower()

    if operacao == 'a':
        resposta = numero_1 + numero_2
        print(f'{resposta=}')
    elif operacao == 'b':
        resposta = numero_1 - numero_2
        print(f'{resposta=}')
    elif operacao == 'c':
        resposta = numero_1 * numero_2
        print(f'{resposta=}')
    elif operacao == 'd':
        resposta = numero_1 / numero_2
        print(f'{resposta=}')
    else:
        print('Opção inválida!')


while True:

    calculadora()
    desejo = input('Digite [s]sair, ou tecle enter para permanecer: ')
    desejo = desejo.lower()
    if desejo == 's':
        quit()

