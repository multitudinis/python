"""
Listas Python

Fatiamento
append, insert, pop, del, clear, extend, 
"""

l1 = [2, 1, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
# metodo usado para juntar 2 listas
l1.extend(l2)
# metodo usado para inserir um valor ao final de uma lista
l1.append('a')
# metodo p inserir valor em determinado indice da lista
l2.insert(3, 'banana')
# exclui o ultimo indice da lista
l2.pop()
# exclui item no indice indicado
del(l1[3])
# exclui item no range indicado
del(l1[3:6])
# cria lista a partir da funçao range
l4 = list(range(0, 10))
# laço for, aplicado a listas
l5 = ['string', True, 3, -3.5]
for elem in l5:
    print(f'O tipo do elemento é {type(elem)}, e seu valor é {elem}')
