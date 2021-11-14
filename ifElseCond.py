# Operadores relacionais em blocos condicionais if else
# Exemplo de liberação de emprestimo

nome = "Mussum branco"
idade = input("Qual a sua idade? ")
idade = int(idade)

# Idade limite para liberação

idadeMinima = 21
idadeMaxima = 80

if idade >= idadeMinima and idade <= idadeMaxima:
    print(f'{nome}, seu emprestimo pode ser considerado.')
else:
    print(f'{nome}, você ainda não tem idade suficiente para essa operação')
