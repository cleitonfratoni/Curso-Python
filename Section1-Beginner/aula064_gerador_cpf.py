import random
import sys

cpf_9_digitos = ''
for i in range(9):
    cpf_9_digitos += str(random.randint(0, 9))

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

cpf_gerado = f'{cpf_9_digitos}-{digito1}{digito2}'

print(cpf_gerado)

# if cpf_usuario == cpf_gerado:
#     print(f'{cpf_usuario} é valido')
# else:
#     print('CPF inválido')
