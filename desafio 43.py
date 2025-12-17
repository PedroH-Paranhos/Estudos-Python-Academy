from style import txt_style,cabeca_style

print('\n',cabeca_style('Desafio 43'),'\n')

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / (altura ** 2)
imc_str = str(imc)

print('Seu IMC é {}'.format(txt_style(imc_str)))

if imc < 18.5:
    print('\n',txt_style('Abaixo do peso!!!'))
elif imc <= 25:
    print('\n',txt_style('Peso do ideal!!!'))
elif imc <= 30:
    print('\n',txt_style('Sobrepeso!!!'))
elif imc <= 40:
    print('\n',txt_style('Obesidade!!!'))
else :
    print('\n',txt_style('Obesidade Mórbida!!!'))
