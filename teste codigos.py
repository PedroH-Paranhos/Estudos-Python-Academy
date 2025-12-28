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

