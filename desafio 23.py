numero = int(input("Digite seu numero: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print("Unidade: \033[96m\033[4m{}\033[0m!".format(unidade))
print("Dezena:  \033[96m\033[4m{}\033[0m!".format(dezena))
print("Centena: \033[96m\033[4m{}\033[0m!".format(centena))
print("Milhar:  \033[96m\033[4m{}\033[0m!".format(milhar))