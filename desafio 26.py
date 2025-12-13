#Faça um programa que leia uma frase pelo tecaldo e mostre:
#quantas vezes aparece a letra "a" / em que posição aparece a primeira vez e ultima.
frase = str(input('Digite uma frase: '))

frase_ajeitada = frase.upper().strip()

contagem = frase_ajeitada.count('A')
primeira_posicao = frase_ajeitada.find('A')
ultima_posicao = frase_ajeitada.rfind('A')

print("A letra 'A' aparece {} vezes ".format(contagem))
print("A Primeira letra 'A' apareceu na posição {} ".format(primeira_posicao))
print("A última letra 'A' apareceu na posição {} ".format(ultima_posicao))
