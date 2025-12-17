from style import txt_style,cabeca_style
from math import trunc

def convert_real (valor):
    return trunc(valor * 100) / 100

print('\n',cabeca_style('Desafio 43'),'\n')

produto = float(input('Digite o valor do produto: '))

desconto_10 = produto * 0.1
desconto_05 = produto * 0.05
juros = produto * 0.2

somente_desconto_10 = '{:.2f}'.format(desconto_10)
somente_desconto_05 = '{:.2f}'.format(desconto_05)
desconto_10_produto = '{:.2f}'.format(produto - desconto_10)
desconto_05_produto = '{:.2f}'.format(produto - desconto_05)
juros_produto = '{:.2f}'.format((produto + juros) / 3)
parcela = produto / 2

condicao = str(input('Escolha '+ txt_style('1') +' para pagamento à vista dinheiro ou cheque:\n'
                      'Escolha '+ txt_style('2') +' para pagamento à vista no cartão: \n'
                      'Escolha '+ txt_style('3') +' para pagamento em até 2x no cartão: \n'
                      'Escolha '+ txt_style('4') +' para pagamento em até 3x ou mais no cartão: \n'))

if condicao == '1':
    print('Seu desconto foi de R${} Total a pagar R${}.'.format(txt_style(str(somente_desconto_10)),
                                                                txt_style(str(desconto_10_produto))))
elif condicao == '2':
    print('Seu desconto foi de R${} Total a pagar R${}.'.format(txt_style(str(somente_desconto_05)),
                                                                txt_style(str(desconto_05_produto))))
elif condicao == '3':
    print('Suas Parcelas ficam de 2x no valor de R${}.'.format(txt_style(str(parcela))))
else :
    print('Suas Parcelas ficam de 3x no valor de R${}.'.format(txt_style(str(juros_produto))))
