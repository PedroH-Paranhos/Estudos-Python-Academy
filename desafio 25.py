#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.
nome = str(input("Qual é seu Nome? "))

nome_sem_espaco = nome.strip()
nome_finalizado = nome_sem_espaco.title()
nome_dividido = nome_sem_espaco.split()

if "Silva" in nome_finalizado:
    print("Seu Nome tem Silva? True")
else:
    print("Seu Nome tem Silva? False")
