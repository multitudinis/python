# Faça um input numerico e diga se é par ou impar

num = input("Digite um numero: ")

try:
    num = int(num)
    parImpar = num % 2

    if parImpar == 1:
        print("O numero é impar")
    else:
        print("O numero é par")
except:
    print("Digite apenas numeros inteiros!")
