# Formatando strings

# positivos
#       [012345678]
texto = 'Python s2'
#      -[987654321]
# negativos

# imprime apenas o caractere na posição indicada do array
print(texto[0])
print(texto[8])
# imprime apenas da posição indicada do array até a segunda posição
print(texto[0:6])
print(texto[:6])  # não é preciso indicar se a posição é a inicial
print(texto[7:9])
print(texto[7:])  # não é preciso indicar se a posição é a final
# imprime retirando apenas o ultimo caractere
print(texto[:-1])
# imprime pulando determinado numero de caracteres indicado apos o segundo dois pontos
print(texto[0:9:2])
print(texto[::2])
