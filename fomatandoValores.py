"""
Formatando valores modificadores

:s - string
:d - int (digit)
:f - float
:.(numero)f - quantidade de casas decimais
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d, f)

> - esquerda
< - direita
^ - centro
"""

num = 10
num2 = 3
divisao = num/num2
nome = 'lucas pessoa'
tag = 'caslu'

print(f"{divisao:.2f}")  # formata quantidade de casa decimais
# formata quantidade de casas decimais com built in format
print("{:.2f}".format(divisao))
print(f'{num:0>10}')  # preenche dez casas com a variavel mais zeros a esquerda
print(f'{num:0<10}')  # preenche dez casas com a variavel mais zeros a direita
# preeche dez casas com a variavel ao centro e zero aos lados
print(f'{num:0^10}')
print(f"{num:.2f}")  # formata quantidade de casas decimais
# preenche dez casas com zeros a direita mais variavel e casas decimais
print(f"{num:0>10.2f}")
print(f"{nome:#>50}")  # preenche 50 casas com cerquilhas a direita
# preenche 50 casas com a variavel ao centro e cerquilhas aos lados
print(f"{nome:#^50}")
# preenche 50 casas com a variavel ao centro e cerquilhas aos lados mas com a built in format
print("{:#^50}".format(nome))
# renomeia a variavel para poder chamala mais de uma vez com a built in format
print('{n:@>13} {n} {0:#^19}'.format(tag, n=nome))
# preenche 13 casas com arrobas e chama a variavel tag pela sua posiçao no array da format
print(nome.lower())  # converte todas as letras da string para minusculas
print(nome.upper())  # converte todas as letras da string para maiusculas
print(nome.title())  # converte as letras iniciais de cada palavra para maiusculas
