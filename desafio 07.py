nota1 = int(input("Digite sua Nota: "))
nota2 = int(input("Digite outra Nota:"))

media = float((nota1 + nota2) / 2)

#ensinamentos da ticy.
resposta = None

if media >= 7: resposta = "Aprovado"
elif media >= 5: resposta = "Em Recuperação"
elif media <= 4: resposta = "Reprovado"

print("Sua media é {}".format(media))
print("Você está {}".format(resposta))

