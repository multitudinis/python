nome = "lucas"
idade = 26
altura = 1.80
peso = 75.75
anoAtual = 2021
birthDate = anoAtual - idade
IMC = peso/altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} KG.')
print(f'O IMC de {nome} é {IMC:.2f}')
print(f'{nome} nasceu em {birthDate}')
print(type(nome))
