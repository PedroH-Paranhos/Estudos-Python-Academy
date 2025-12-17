from style import txt_style
import random

escolha_1 = 'Pedra'
escolha_2 = 'Papel'
escolha_3 = 'Tesoura'

escolha = str(input('Escolha {} para Pedra.'
                    ' Escolha {} para Papel.'
                    ' Escolha {} para Tesoura.\n '.format(txt_style(escolha_1),txt_style(escolha_2),txt_style(escolha_3))))

escolha_title = escolha.title()
escolha_python = random.choice(['Pedra','Papel','Tesoura'])

print('Minha escolha é {} e a sua é {}'.format(escolha_python,escolha_title))

if escolha == escolha_python:
    str(input('Escolha {} para Pedra.'
              ' Escolha {} para Papel.'
              ' Escolha {} para Tesoura.\n '.format(txt_style(escolha_1), txt_style(escolha_2), txt_style(escolha_3))))
elif escolha_title == escolha_1 and escolha_python == escolha_2:
    print('Você Perdeu!!')
elif escolha_title == escolha_1 and escolha_python == escolha_3:
    print('Você Ganhou!!')
elif escolha_title == escolha_2 and escolha_python == escolha_1:
    print('Você Ganhou!!')
elif escolha_title == escolha_2 and escolha_python == escolha_3:
    print('Você Perdeu!!')
elif escolha_title == escolha_3 and escolha_python == escolha_1:
    print('Você Perdeu!!')
else :
    print('Você Ganhou!!')
