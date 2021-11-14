# Peça ao usuario que digite seu nome, de acordo com a quantidade de letras
# afirme se é um nome curto, normal ou longo

nome = input("Digite seu primeiro nome: ")
nomeLeng = len(nome)

if nomeLeng <= 4:
    print("Seu nome é curto")
elif nomeLeng == 5 or nomeLeng == 6:
    print("Seu nome é normal")
elif nomeLeng >= 7:
    print("Seu nome é longo")
