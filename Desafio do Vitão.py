valor = int(input("Digite seu Número: "))

resultado = True

if valor <= 1: resultado = False

for numero in range(2, (valor // 2) + 1):
    if valor % numero == 0:
        resultado = False
        break

print("Seu numero é Primo ?")
print("{}".format(resultado))
