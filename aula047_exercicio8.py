import os

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai porpor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a palavra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na pavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário
"""

secreta = 'pepi'
plv_formatada = '*' * len(secreta)
letra_digitada = ''
indice = 0
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    ver_letra = len(letra_digitada)
    
    if ver_letra > 1:
        print('Digite apenas uma letra')
        continue
    else:
        for j in secreta:
            if letra_digitada == j:
                plv_formatada = plv_formatada[:indice] + j + plv_formatada[indice + 1 :]
            indice += 1
        print(f'Palavra formatada: {plv_formatada}')
    indice = 0
    tentativas += 1
    if plv_formatada == secreta:
        plv_formatada = '*' * len(secreta)
        os.system("clear")
        print('VOCÊ GANHOU PARABÉNS!!')
        print(f'A palavra é {secreta}')
        print(f'Tentativas: {tentativas}')
        tentativas = 0
