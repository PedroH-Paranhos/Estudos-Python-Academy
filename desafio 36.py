#escreva um programa para provar o emprestimo bancario para a compra de uma casa, o programa deve perguntar;
#o valor da casa, o salario do comprador e em quantos anos ela vai pagar.calcule a prestação mensal
#sabendo que ela não pode exceder 30% do salario então o emprestimo sera negado
#qual o valor minimo de salário necessario para a prestação se igualar a 30% do salário
print('=-= \033[4m\033[96mDESAFIO 36\033[0m =-=')

valor_imovel = float(input('\nQual o Valor do Imovel? '))
salario = float(input('\nQual o Valor do Salário? '))
meses = int(input('\nQuantos meses de financiamento? '))

entrada = valor_imovel * 0.3
prestacao = (valor_imovel - entrada) / meses
min_prestacao = salario * 0.3
min_salario = prestacao / 0.3

if prestacao <= min_prestacao:
    print('\nSeu emprestimo foi aprovado!')
    print('Sua entrada deve ser de R${:.2f} !'.format(entrada))
    print('Sua prestação ficara no valor de R${:.2f} !'.format(prestacao))
    print('Sua Prestação maxima a se pagar é de R${:.2f} !'.format(min_prestacao))
    print('Seu Salário minimo pode ser de R${:.2f} !'.format(min_salario))
else:
    print('\nSeu emprestimo foi reprovado!')
    print('Sua entrada deve ser de R${:.2f} !'.format(entrada))
    print('Sua prestação ficara no valor de R${:.2f} !'.format(prestacao))
    print('Sua Prestação Real é de R${:.2f} !'.format(min_prestacao))
    print('Seu Salário minimo pode ser de R${:.2f} !'.format(min_salario))