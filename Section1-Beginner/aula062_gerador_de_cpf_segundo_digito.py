"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf_usuario = '36323824833'
cpf_9_digitos = cpf_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito1 in cpf_9_digitos:
    resultado_digito_1 += int(digito1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito1 = (resultado_digito_1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

cpf_com_digito1 = cpf_9_digitos + str(digito1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito2 in cpf_com_digito1:
    resultado_digito_2 += int(digito2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito2 = (resultado_digito_2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpf_gerado = f'{cpf_9_digitos}{digito1}{digito2}'

if cpf_usuario == cpf_gerado:
    print(f'{cpf_usuario} é valido')
else:
    print('CPF inválido')
