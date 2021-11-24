"""
Split gera iteraveis a partir de uma string
"""

string = 'o brasil é um pais do futuro'
lista = string.split(' ')
lista2 = string.split('um')
# print(lista)

for str in lista:
    print(str)

for str in lista2:
    print(str)

string2 = 'qualquer coisa é a mesma coisa porque tudo é a mesma coisa'
lista3 = string2.split(' ')

for str in lista3:
    print(f'a palavra {str}, apareceu {lista3.count(str)}x na lista')

palavra = ''
contagem = 0

for valor in lista3:
    qtd_vezes = lista3.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(
    f'A palavra {palavra}, apareceu mais vezes. Num total de {qtd_vezes} vezes')

# a função strip() remove " " espaços no inicio e no final de strings
teste = ' aaa '
print(teste.strip())

# join() insere um elemento entre os itens em uma lista

lista4 = '.'.join(lista)
print(lista4)

# enumerate() cria um indice para os itens da lista
for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

# exemplo de desempacotamento
string3 = 'um dois trez'
lista5 = string3.split(' ')
i1, i2, i3 = lista5
print(i2)
