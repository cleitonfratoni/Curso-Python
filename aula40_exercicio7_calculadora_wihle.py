"""Calculadora com while"""
while True:
    numero_1 = input('Digite um número: ')
    numeor_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validors = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numeor_2)
        numeros_validors = True
    except:
        numeros_validors = None
    
    if numeros_validors is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo:')
    
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float }=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')  
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break