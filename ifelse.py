# a sintaxe dos blocos if else é feita por 4 espaços ou um TAB
# apos descer uma linha que indica um bloco
# elif é abreviação de else if
# caso nenhuma condição seja verdadeira, o else será executado
if False:
    print("Não vou fazer nada")
elif False:
    print("Agora to disposto!")
else:
    print("Vou assim mesmo...")

# quando uma condição é verdadeira o comando será executado
# e o bloco if else termina.

if True:
    print("Larguei mais cedo")
    num = 2
    num2 = 3
    print(num+num2)
elif False:
    print("Quem viu viu!")
elif True:
    print("Cheguei tarde.")
else:
    print("Já é qualquer coisa")

# Operadores Relacionais
# == > >= < <= !=

num = 2
num2 = 2
var = "lucas"
var2 = "pessoa"

expressao = (num == num2)
print(expressao)
expressao2 = (num >= num2)
print(expressao2)
expressao3 = (num <= num2)
print(expressao3)
expressao4 = (num != num2)
print(expressao4)
expressao5 = (var < var2)
print(expressao5)

# Operadores Lógicos
# and, or, not, in e not in

if expressao and expressao2:
    print("Tudo verdade")
if expressao or expressao4:
    print("Tem alguma verdade")

# o not so inverte o argumento imediatamente seguinte
# if not num > num2 and not var > var2:
if not (num > num2 and var < var2):
    print(num > num2)
    print(var > var2)
    print("Algo não é verdade")

if not num > num2 or var > var2:
    print("Algo não é verdade")

if "uc" in var:
    print("Contém o fragmento")

if "22" not in var2:
    print("Fragmento não encontrado")
