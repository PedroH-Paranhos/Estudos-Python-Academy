import random

primeiro_aluno = input("Primeiro aluno: ")
segundo_aluno = input("Segundo aluno: ")
terceiro_aluno = input("Terceiro aluno: ")
quarto_aluno = input("Quarto aluno: ")

aluno_sorteio = random.choice([primeiro_aluno,segundo_aluno,terceiro_aluno,quarto_aluno])

print("O aluno sortiado foi {} !!".format(aluno_sorteio))
