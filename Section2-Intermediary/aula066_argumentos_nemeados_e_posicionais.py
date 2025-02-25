"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)


soma(10, 23, 4)
soma(y=23, z=4, x=10)

print(10, 23, 4, sep='-')