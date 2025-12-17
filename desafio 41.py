ano_calendario = int(input('Qual ano atual do calendario? '))
ano = int(input('Qual ano voce nasceu? '))

idade = ano_calendario - ano
infantil = idade

if idade <= 9 :
    print('\nMIRIM')
elif idade <= 14 :
    print('\nINFANTIL')
elif idade <= 19 :
    print('\nJUNIOR')
elif idade <= 20 :
    print('\nSENIOR')
else :
    print('\nMASTER')
