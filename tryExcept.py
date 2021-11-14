# Como evitar possiveis erros gerados pelo usuario
num = input("Digite um numero: ")
num2 = input("Digite um numero: ")

try:
    num = float(num)
    num2 = float(num2)

    print(num - num2)
except:
    print("Error!")

# Place holders

condiçao = True

if not condiçao:
    # Vou criar uma ação depois
    pass
if not condiçao:
    # Vou criar uma ação depois
    ...
else:
    print("Passei sem codigo e sem erro")
