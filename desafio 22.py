nome = str(input("Digite o nome completo: "))

nome_minusculo = nome.lower()
nome_maiusculo = nome.upper()
nome_sem_espaco = nome.replace(" ","")
nome_quantidade = len(nome_sem_espaco)
nome_dividido = nome.split()
primeiro_nome = nome_dividido[0]

print("Seu nome é '\033[4m{}\033[0m'".format(nome))
print("Seu nome Maiúscula é '\033[4m{}\033[0m'".format(nome_maiusculo))
print("Seu nome Minúsculo é '\033[4m{}\033[0m'".format(nome_minusculo))
print("Seu nome sem espaços é '\033[4m{}\033[0m'".format(nome_sem_espaco))
print("Quantas letras tem seu Nome: '\033[4m{}\033[0m'".format(nome_quantidade))
print("Somente seu Primeiro Nome: '\033[4m{}\033[0m'".format(primeiro_nome))