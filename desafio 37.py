#escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário 2 para octal 3 para hexadecimal
print('=-= \033[4m\033[96mDESAFIO 36\033[0m =-=')

numero = int(input('\nDigite seu Número: '))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

conversao = int(input('\nEscolha \033[4m\033[96m1\033[0m para Binário,'
                      ' \033[4m\033[96m2\033[0m para Octal,'
                      ' \033[4m\033[96m3\033[0m para Hexadecimal. '))

if conversao == 1:
    print('\nSeu número em Binário: \033[4m\033[96m{}\033[0m'.format(binario))
elif conversao == 2:
    print('\nSeu número em Octal: \033[4m\033[96m{}\033[0m'.format(octal))
else :
    print('\nSeu número em Hexadecimal: \033[4m\033[96m{}\033[0m'.format(hexadecimal))
