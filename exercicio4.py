# Jogo da forca, sem forca e sem desenho :P
secreto = 'perfume'
digitadas = []
chances = 3
while True:

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print('Isso não vale, digite só uma letra')
        continue
    elif letra in secreto:
        print('Muito bem, você advinhou uma letra')
        digitadas.append(letra)
    else:
        print('letra não existe na palavra secreta')
        chances -= 1
        if chances == 0:
            print('Você perdeu')
            break
        print(f'Você tem mais {chances} chances')

    secretoTemporario = ''
    for letraSecreta in secreto:
        if letraSecreta in digitadas:
            secretoTemporario += letraSecreta
        else:
            secretoTemporario += '*'
    if secretoTemporario == secreto:
        print(f'Você conseguiu, a palavra é: {secreto}')
        break
    else:
        print(f'Até agora você descobriu essas letras: {secretoTemporario}')
