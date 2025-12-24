from style import cabeca_style

print(cabeca_style('LOJA DO PEDRÃO'))

soma = menor_p = maior_p = cont = 0
barato = ''
while True :
    produto = str(input('\nDigite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))
    cont += 1
    soma += preco

    if preco >= 1000 :
        maior_p += 1
    if cont == 1 or preco < menor_p :
        menor_p = preco
        barato = produto

    resposta = " "
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N' :
        break

print(f'{cabeca_style('FIM DO PROGRAMA')}')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maior_p} produtos custando mais de R$1000.00')
print(f'o produto mais barato custa R${menor_p:.2f} ')
