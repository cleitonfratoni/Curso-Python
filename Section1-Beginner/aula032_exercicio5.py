"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímar. Caso  usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

from curses.ascii import isdigit

# val_digitado = input('Digite um numero inteiro: ')

# if val_digitado.isdigit():
#     par_ou_impar = int(val_digitado) % 2
#     if par_ou_impar == 0:
#         print(f'O número {val_digitado} é par.')
#     else:
#         print(f'O número {val_digitado} é impar.')
# else:
#     print('O valor digitado não é valido.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite a hora: ')

# try:
#     hora = int(entrada)
    
#     if hora >= 0 and hora <=11:
#         print('Bom dia!')
        
#     elif hora > 11 and hora <= 17:
#         print('Boa tarde!')
        
#     elif hora > 17 and hora <= 23:
#         print('Boa noite')
        
#     else:
#         print('Não conheço esta hora')
# except:
#     print('O valor digitado é invalido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

# nome = input('Digite seu primeiro nome: ')

# nome_tamanho = len(nome)

# if nome_tamanho > 1:
#     if nome_tamanho <= 4:
#         print("Seu nome é curto")
#     elif nome_tamanho > 4 and nome_tamanho <= 6:
#         print("Seu nome é normal")
#     else:
#         print("Seu nome é muito grande")
# else:
#     print("Digite mais de uma letra.")