# Laço infinito
while False:  # true
    nome = input("Qual o seu nome? ")
    print(f"{nome}")

x = 3
while x < 3:
    print(x)
    x = x + 1

y = 3
while y < 3:
    print(y)
    if y == 2:
        continue  # pula para o proximo laço sem executar os codigos abaixo
    y = y + 1

z = 3
while z < 3:
    print(z)
    z += 1
    if z == 2:
        break  # para a execução do laço onde está
        print("Não vai ser executando.")
    print("executando...")

a = 10
while a < 10:
    s = 0
    while s < 5:
        print(f'{a} {s}')
        s += 1
    a += 1

while True:
    continuar = input('A calculadora será iniciada, deseja continuar? [s/n] ')
    if continuar == 'n':
        print('Programa encerrado.')
        break
    num = input("Digite um numero: ")
    num2 = input("Digite um numero: ")
    operador = input("Digite um operador: ")

    if not num.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um numero')
        continue

    num = int(num)
    num2 = int(num2)

    if operador == '+':
        print(num + num2)
    elif operador == '-':
        print(num - num2)
    elif operador == '*':
        print(num * num2)
    elif operador == '/':
        print(num / num2)
    else:
        print("Operador invalido!")

"""contador = 0
acumulador = 0

while contador < 0:
    print(contador)
    contador += 1
    acumulador = acumulador + contador
    if contador == 11:
        break
else:
    print('Não vai ser executado.')
print('Aqui o break não age.')
"""

frase = 'o rato roeu a roupa do rei de roma'
tamanhoFrase = len(frase)
contador = 0
novaFrase = ''

while contador < tamanhoFrase:
    print(frase[contador], contador)
    letra = frase[contador]
    if letra == 'r':
        novaFrase += 'R'
    else:
        novaFrase += letra
    contador += 1
print(novaFrase)
