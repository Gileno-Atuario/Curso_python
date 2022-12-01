palavra_secreta = 'FUTEBOL'
letras_certas = ''


while True:

    letra_digitada = input('Digite uma letra: ').strip()
    letra_trabalhada = letra_digitada.upper()
    visualizacao = ''

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

    print(f'{visualizacao}\n')

    if visualizacao == palavra_secreta:
        print('PARABÉNS🎉🎉🎉')
        quit()

