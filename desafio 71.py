import datetime
import time
from style import (cabeca_style, divisao_style,
                   txt_style_azul, txt_style_vemelho,
                   txt_style_amarelo, txt_style_verde,
                   ampulha_style, divisao_style_time)
from random import choices
import easygui
import tkinter as tk
from tkinter import simpledialog

print(f'{cabeca_style('Algoritimo de Saque no Caixa Eletrônico')}\n')
print(f'{divisao_style()}\n')

print(f'{cabeca_style('Bem-Vindo ao Banco do Brasil')}\n')
str(input(f'{txt_style_azul('Pressione "Enter" para Prosseguir.')}'))

resposta = ''
while resposta != 'SAQUE':  # <----- loop de interface de escolha
    resposta = easygui.buttonbox(
        "Escolha Dentre as Opções a que mais lhe Atende.",
        choices=["SAQUE", "SALDO", "TRANSFERÊNCIA", "OUTROS SERVIÇOS"],
        title="ALGORITIMO DE SAQUE NO CAIXA ELETRONICO"
    )

print(f"\nVocê escolheu: {txt_style_azul(resposta)}\n")
print(f"{txt_style_amarelo("Insira o Cartão")}")
print(f'\/ ' * 5)

time.sleep(4)
print(f'\nAltenticando validade do cartão, Porfavor aguarde.')

ampulha_style() # <----  ampulheta

divisao_style_time() #<---- divisão estilizada com timer

print(f'\n{txt_style_verde('Altenticação feita com sucesso')}')
time.sleep(2.5)

print(f"\n{txt_style_amarelo("Insira o Senha Cartão")}")
#----------------------------------------------------------------
root = tk.Tk()
root.withdraw()

opcoes = [""]
senha_resposta = simpledialog.askstring("BANCO DO BRASIL",
                                  "POR FAVOR, DIGITE SUA SENHA:\n" + "\n".join(opcoes))
#-----------------------------------------------------------------
time.sleep(2.5)

print(f'\nAltenticando validade de senha, Porfavor aguarde.')

ampulha_style() # <----  ampulheta

divisao_style_time() #<---- divisão estilizada com timer

print(f'\n{txt_style_verde('Altenticação feita com sucesso\n')}')
time.sleep(3)
#----------------------------------------------------------------
valores_resposta = easygui.buttonbox( # <----- box de escolha para valores
    "Escolha o Valor para o Saque.",
    choices=["200", "100", "80", "50", "30", "Outros Valores"],
    title="ALGORITIMO DE SAQUE NO CAIXA ELETRONICO / Valores"
)

if valores_resposta == "Outros Valores":
    while True:
        outros_valores = easygui.enterbox( "Por Favor, Digite o Montante Desejado:",)

        if outros_valores is None:
            easygui.msgbox('Operação Cancelada, Retire o Cartão e Refaça a Validação', 'Transação Cancelada')
            break
        try:
            numero = int(outros_valores)
            confirmacao_saque = easygui.buttonbox(
                msg = f'✓ Número válido: R${numero},00 , Deseja Continuar?',
                title = 'Confirmação',
                choices = ["Sim", "Não"]
            )
            if confirmacao_saque == "Sim":
                valores_resposta = numero
                break
            else:
                easygui.msgbox(f'Confirmação do Valor a Sacar Cancelado. Insira um novo valor')
        except ValueError:
            easygui.msgbox(f'✗ Isso não é um número inteiro!\nTente novamente.', 'Erro')

valores_resposta = int(valores_resposta)
def contar_cedulas_basico(valor):
    cedulas = [200, 100, 50, 20, 10, 5, 2]
    resultado = {}
    valor_restante = valor

    print(f"Valor: R$ {valor:.2f}")
    print("-" * 30)

    for cedula in cedulas:
        if valor_restante >= cedula:
            quantidade = valor_restante // cedula
            resultado[cedula] = quantidade
            valor_restante %= cedula  # Resto da divisão
            print(f"{quantidade} cédula(s) de R$ {cedula:.2f}")

    if valor_restante > 0:
        print(f"↳ Restante: R$ {valor_restante:.2f} (não há cédula para isso)")

    return resultado

time.sleep(1.5)
contar_cedulas_basico(valores_resposta)
#----------------------------------------------------------------------------
print(f'\n{txt_style_vemelho("Retire o Dinheiro.")}')
time.sleep(1.5)

comprovante = easygui.buttonbox(
    msg = f'Deseja Comprovante da Transação?',
    title = 'Comprovante de Transação',
    choices =["Sim", "Não"]
)
if comprovante != 'Sim':
    finalizacao = easygui.buttonbox(
        msg = f'Você optou por não ter o comprovante, deseja realizar outra movimentação?',
        title = 'Finalização',
        choices = ["Sim", "Não"]
)
    if finalizacao == "Sim":
        print(f'{txt_style_verde('Voltando para o menu de Inicial, Muito Obrigado')}')
    else:
        print(f'Muito Obrigado, Volte sempre.')
else:
    print(txt_style_amarelo('Gerando Comprovante...'))

    ampulha_style()

    print(f"┌─────────────────────────────────────────────┐")
    print(f"│          Comprovante de Transação           │")
    print(f"├─────────────────────────────────────────────┤")
    print(f"│ Banco do Brasil                             │")
    print(f"│ Data: ............      Hora: 14:30         │")
    print(f"│ Caixa: 03             Cupom: 000123         │")
    print(f"├─────────────────────────────────────────────┤")
    print(f"│ Produto           Qtd  Unitário    Total    │")
    print(f"├─────────────────────────────────────────────┤")
    print(f"│ Subtotal:                      R$ ??????    │")
    print(f"│ Desconto:                      R$  ?????    │")
    print(f"│ Total:                         R$  ??  ???  │")
    print(f"└─────────────────────────────────────────────┘")

