frase = input('Digite a palavra ou texto: ')
frase_minuscula = frase.lower()

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    contagem_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < contagem_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = contagem_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'\tA letra [{letra_apareceu_mais_vezes}] foi a que mais apareceu,\n '
      f'com o total de {qtd_apareceu_mais_vezes} aparições.')


