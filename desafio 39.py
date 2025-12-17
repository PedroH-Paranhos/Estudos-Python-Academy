ano_calendario = int(input('Qual ano atual do calendario? '))
ano = int(input('Qual ano voce nasceu? '))

idade = ano_calendario - ano
passou = idade - 17
falta = 17 - idade

print('Você tem {} anos.'.format(idade))

if idade == 17:
    print('\nJa está na hora de voce se alistar!!')
elif idade >= 18:
    print('\nja passou {} anos do prazo de alistamento!!'.format(passou))
else :
    print('\nainda falta {} anos para se alistar!!'.format(falta))
