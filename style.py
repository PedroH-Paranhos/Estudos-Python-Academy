import time

style = {
    'subli': '\033[4m',
    'azul': '\033[96m',
    'reset': '\033[0m',
    'vermelho': '\033[91m',
    'amarelo' : '\033[93m',
    'verde' : '\033[92m'
}

def txt_style_azul (texto):
    return style['subli'] + style['azul'] + texto + style['reset']

def txt_style_vemelho (texto):
    return style['subli'] + style['vermelho'] + texto + style['reset']

def txt_style_verde (texto):
    return style['subli'] + style['verde'] + texto + style['reset']

def txt_style_amarelo (texto):
    return style['subli'] + style['amarelo'] + texto + style['reset']

def cabeca_style (texto):
    return ('='*5) + txt_style_azul(texto) + ('='*5)

def divisao_style ():
    return '-===-'*10

def divisao_style_time ():
    time.sleep(1.5)
    print(f'\n~s~   ~s~   ~s~   ~s~' * 2)
    time.sleep(2.5)

def ampulha_style ():
    frames = ['⌛', '⏳', '⏳', '⌛']
    angles = ['◢', '◣', '◤', '◥']
    i = 0
    start_time = time.time()
    while time.time() - start_time < 3:
        print(f'\r{angles[i % 4]} {frames[i % 2]} {angles[i % 4]}', end='', flush=True)
        i += 1
        time.sleep(0.2)


