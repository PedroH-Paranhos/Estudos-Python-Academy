style = {
    'subli': '\033[4m',
    'azul': '\033[96m',
    'reset': '\033[0m'
}

def txt_style (texto):
    return style['subli'] + style['azul'] + texto + style['reset']

def cabeca_style (texto):
    return ('='*5) + txt_style(texto) + ('='*5)
