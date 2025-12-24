from style import cabeca_style

print(cabeca_style('CADASTRE UMA PESSOA'))

demaior = 0
homens = 0
mulheres = 0

while True:
    idade = int(input(f"\nIdade: "))
    sexo = str(input(f"Sexo [M/F]: ")).strip().upper()
    continuar = str(input(f"Deseja continuar? [S/N]: ")).strip().upper()

    if idade > 18:
        demaior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    if continuar == 'N':
         break

print(f'\nTotal de pessoas com mais de 18 anos: {demaior} ')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulher com menos de 20 anos')
