texto = 'Python'
for letra in texto:
    print(letra)

# Built in RANGE

for n in range(10):
    print(n)

# (1(começo da contagem), 2(final da contagem), 3(incremento ou decremento))
for n in range(20, 10, -1):
    print(n)

texto2 = ''
for letra in texto:
    if letra == 't':
        texto2 += 'T'
    elif letra == 'h':
        texto2 = texto2 + letra.upper()
    else:
        texto2 += letra
print(texto2)

textos = ['qualquer', 'python', 'um']
for palavra in textos:
    if palavra.lower().startswith('p'):
        print('começa com p')
        break  # se o laço não for quebrado o else sera executado
    print(palavra)
else:
    print("não começa com P")
