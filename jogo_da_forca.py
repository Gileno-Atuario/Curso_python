palavra_secreta = 'FUTEBOL'
total_letras = len(palavra_secreta)
letras_certas = ''
tentativas = 0
total_tentativas = 15
print(f'-----JOGO DA FORCA-----\nA palavra secreta possui {total_letras} letras.\n'
      f'Você possui {total_tentativas} chances.\nBoa Sorte!\n')

while True:

    letra_digitada = input('Digite uma letra: ').strip()
    letra_trabalhada = letra_digitada.upper()
    visualizacao = ''
    tentativas += 1
    chances = total_tentativas - tentativas

    if len(letra_trabalhada) != 1 or not letra_trabalhada.isalpha():
        print('Digite apenas um letra!\n')
        continue
    
    if letra_trabalhada in palavra_secreta:
        letras_certas += letra_trabalhada
        print('Você ACERTOU 😁')
    else:
        print('Você ERROU 😭')

    for letras_secreta in palavra_secreta:
        if letras_secreta in letras_certas:
            visualizacao += letras_secreta
        else:
            visualizacao += '*'

    print(f'\t\t{visualizacao}\n')

    if chances < 0:
        print('VOCÊ PERDEU! TENTE OUTRA VEZ!')
        quit()

    if visualizacao == palavra_secreta:
        print('VOCÊ GANHOU! PARABÉNS!🎉🎉🎉')
        quit()

    print(f'Ainda lhe resta {chances} chanche(s).\n')
